import json
from utils.util import Util
from utils.utilsocket import UtilSocket
from btc.block import Block
from btc.transaction import Transaction


def main():
    log = Util.get_logger("client")

    url = "ws://ws.blockchain.info/inv"
    url_raw_block = "https://blockchain.info/rawblock/"
    url_raw_tx = "https://blockchain.info/rawtx/"

    with UtilSocket(url) as usocket:
        # blocks
        ping_block = {
            "op": "ping_block"
        }
        log.info("message_payload={}".format(json.dumps(ping_block)))

        response = usocket.send(json.dumps(ping_block))
        block = Block(response)
        # log.info("block.repr={}".format(repr(block)))
        log.info("block.str={}".format(str(block)))

        # transactions
        ping_tx = {
            "op": "ping_tx"
        }
        log.info("message_payload={}".format(json.dumps(ping_tx)))

        response = usocket.send(json.dumps(ping_tx))
        tx = Transaction(response)
        # log.info("tx.repr={}".format(repr(tx)))
        log.info("tx.str={}".format(str(tx)))
        log.info("tx.input_values={}".format(tx.input_values))
        log.info("tx.output_values={}".format(tx.output_values))


if __name__ == "__main__":
    main()
