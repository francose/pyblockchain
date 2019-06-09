'''
Author : Sadik Erisen
Date : Feb.6th 2018
Purpose : The purpopse of this module to create parameters and combine with the giving data
'''
import create as c
import test as t
import data_pack as dp

#Global variables

Genesis_Index = 0
Genesis_previous_hash = '0'
Genesis_timestamp = 1495851743

Genesis_data = 'first block'

class BlockParams():

    def __init__(self, index, previous_hash, timestamp, data):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.data = data

    def __str__(self):
        return str(self.index) + self.previous_hash + str(self.timestamp) + self.data

    @classmethod
    def genesis_params(cls):
        return cls(GENESIS_INDEX, GENESIS_PREVIOUS_HASH, GENESIS_TIMESTAMP, GENESIS_DATA)
