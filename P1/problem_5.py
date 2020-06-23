# -*- coding: utf-8 -*-
# problem_5.py
# Author: Matheus Dal Mago
# 2020

import hashlib
import datetime


class Block:
    def __init__(self, timestamp, data, previous_hash):
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash()

    def calc_hash(self):
        sha = hashlib.sha256()
        hash_str = self.data.encode('utf-8')
        sha.update(hash_str)
        return sha.hexdigest()

    def __repr__(self):
        return f"Block({self.data})"


class ChainNode:
    def __init__(self, node):
        self.node = node
        self.next = None

    def __repr__(self):
        return str(self.node)


class BlockChain:
    def __init__(self):
        self.chain_head = None
        self.chain_tail = None

    def add_transaction(self, timestamp, data):
        if self.chain_head is None:  # First element in the chain
            block = Block(timestamp, data, 0)
            node = ChainNode(block)
            self.chain_head = node
            self.chain_tail = node

        else:  # Add to the end of the chain
            block = Block(timestamp, data, self.chain_tail.node.hash)  # Get hash of previous node
            node = ChainNode(block)
            self.chain_tail.next = node
            self.chain_tail = node

    def __repr__(self):
        out_str = ""
        node = self.chain_head
        while node:
            out_str += str(node) + " -> "
            node = node.next

        return out_str


def get_utc_time():
    return str(datetime.datetime.utcnow())

if __name__ == "__main__":
    block_chain = BlockChain()

    block_chain.add_transaction(get_utc_time(), "first transaction")
    block_chain.add_transaction(get_utc_time(), "second transaction")
    block_chain.add_transaction(get_utc_time(), "third transaction")

    print(block_chain)  # All the chains
    print(block_chain.chain_head.node.data)  # "first transaction"
    print(block_chain.chain_head.node.hash)  # hash of "first transaction"

    block_chain2 = BlockChain()  # empty block chain
    print(block_chain2)

    block_chain3 = BlockChain()
    block_chain3.add_transaction(get_utc_time(), "")  # empty data
    block_chain3.add_transaction(get_utc_time(), "data2")

    print(block_chain3.chain_tail.node.previous_hash)  # hash of ""
