import json
from utils.util import Util
from utils.utilsocket import UtilSocket


def main():
    log = Util.get_logger("client")

    url = "ws://ws.blockchain.info/inv"
    url_raw_block = "https://blockchain.info/rawblock/"
    url_raw_tx = "https://blockchain.info/rawtx/"

    usocket = UtilSocket(url)

    ping = {
        "op": "ping_block"
    }
    log.info("message_payload={}".format(json.dumps(ping)))

    response = usocket.send(json.dumps(ping))
    log.info("ping_response={}".format(response))

    block = json.loads(response)
    log.info("tx_count={}".format(len(block["x"]["txIndexes"])))
    log.info("nTx={}".format(block["x"]["nTx"]))
    log.info("totalBTCSent={}".format(block["x"]["totalBTCSent"]/100000000))
    log.info("height={}".format(block["x"]["height"]))
    log.info("foundBy.link={}".format(block["x"]["foundBy"]["link"]))

    block_tx_id = block["x"]["foundBy"]["link"].split("/")[-1]
    log.info("block_tx_id={}".format(block_tx_id))


if __name__ == "__main__":
    main()
