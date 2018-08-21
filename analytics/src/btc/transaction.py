import json
from utils.util import Util


class Transaction:
    def __init__(self, payload):
        self.log = Util.get_logger("Transaction")
        self.payload = payload

        self.size = self.dict()["size"]
        self.input_count = len(self.dict()["inputs"])
        self.input_values = [in_dict["prev_out"]["value"] for in_dict in self.dict()["inputs"]]
        self.output_count = len(self.dict()["out"])
        self.output_values = [out_dict["value"] for out_dict in self.dict()["out"]]

    def __repr__(self):
        return self.payload

    def __str__(self):
        return "size={}, input_count={}, output_count={}"\
            .format(self.size, self.input_count, self.output_count)

    def dict(self):
        return json.loads(self.payload)["x"]
