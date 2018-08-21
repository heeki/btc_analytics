import json
import time
import websocket
from threading import Thread
from util import Util


class UtilSocket:
    def __init__(self, url):
        self.log = Util.get_logger("UtilSocket")
        self.host = url

    def __enter__(self):
        self.log.info("initiating connection to {}".format(self.host))
        self.ws = websocket.create_connection(self.host)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.log.info("closing connection to {}".format(self.host))
        self.ws.close()

    def send(self, msg):
        self.ws.send(msg)
        result = self.ws.recv()
        return result

    def forever(self):
        websocket.enableTrace(True)
        self.ws.run_forever()


class UtilSocketApp(websocket.WebSocketApp):
    def __init__(self):
        self.log = Util.get_logger("UtilSocketApp")

    def on_message(self, message):
        self.log.info(message)

    def on_error(self, error):
        self.log.error(error)

    def on_close(self):
        self.log.info("closed")

    def on_open(self):
        def run(*args):
            ping = {
                "op": "ping"
            }
            for i in range(3):
                self.send(json.dumps(ping))
                time.sleep(1)
            time.sleep(1)
            self.close()
            self.log.info("thread terminating")

        Thread(target=run).start()
