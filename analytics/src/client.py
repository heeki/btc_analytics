import json
from utils.utilsocket import UtilSocket


def main():
    url = "ws://ws.blockchain.info/inv"
    url_raw_block = "https://blockchain.info/rawblock/"
    url_raw_tx = "https://blockchain.info/rawtx/"

    usocket = UtilSocket(url)

    ping = {
        "op": "ping_block"
    }
    print "message_payload={}".format(json.dumps(ping))

    response = usocket.send(json.dumps(ping))
    print "ping_response={}".format(response)

    block = json.loads(response)
    print "tx_count={}".format(len(block["x"]["txIndexes"]))
    print "nTx={}".format(block["x"]["nTx"])
    print "totalBTCSent={}".format(block["x"]["totalBTCSent"]/100000000)
    print "height={}".format(block["x"]["height"])
    print "foundBy.link={}".format(block["x"]["foundBy"]["link"])

    block_tx_id = block["x"]["foundBy"]["link"].split("/")[-1]
    print "block_tx_id={}".format(block_tx_id)


if __name__ == "__main__":
    main()
