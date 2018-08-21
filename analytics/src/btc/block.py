import json
from utils.util import Util


class Block:
    def __init__(self, payload):
        self.log = Util.get_logger("Block")
        self.payload = payload

        self.height = self.dict()["height"]
        self.total_tx = self.dict()["nTx"]
        self.total_btc_sent = self.dict()["totalBTCSent"] / 100000000
        self.found_by_link = self.dict()["foundBy"]["link"]
        self.found_by_tx_id = self.found_by_link.split("/")[-1]

    def __repr__(self):
        return self.payload

    def __str__(self):
        return "height={}, total_tx={}, total_btc_sent={}, found_by_link={}, found_by_tx_id={}"\
            .format(self.height, self.total_tx, self.total_btc_sent, self.found_by_link, self.found_by_tx_id)

    def dict(self):
        return json.loads(self.payload)["x"]
