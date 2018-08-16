import json
import socket
import ssl
import time
import urllib2
from util import Util


class UtilAPI:
    def __init__(self):
        self.log = Util.get_logger("UtilAPI")

    def get_data(self):
        while True:
            try:
                data = urllib2.urlopen(self.url, timeout=3).read()
                break
            except ssl.SSLError as e:
                self.log.info("get_data(): ssl.SSLError {}".format(e))
            except urllib2.URLError as e:
                self.log.info("get_data(): urllib2.URLError {}".format(e))
            except socket.error as e:
                self.log.info("get_data(): socket.error {}".format(e))
            time.sleep(3)
        return json.loads(data)
