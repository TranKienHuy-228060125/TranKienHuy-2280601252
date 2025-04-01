import hashlib
import json

class Block:
    def __init__(self, index, timestamp, transactions, previous_hash, proof):
        self.index = index
        self.timestamp = timestamp
        self.transactions = transactions
        self.previous_hash = previous_hash
        self.proof = proof

    def compute_hash(self):
        """
        Tính toán hash cho khối hiện tại bằng cách băm nội dung của nó.
        """
        block_string = json.dumps(self.__dict__, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()
