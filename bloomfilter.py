import math
import mmh3
from bitarray import bitarray

class BloomFilter(object):
    def __init__(self, expected_item_count: int, fp_prob : float):
        '''
        expected_item_count: Number of items expected to be stored in the filter
        
        fp_prob: False Positive probability
        
        '''
        self.fp_prob = fp_prob
        self.size = BloomFilter.get_size(expected_item_count, fp_prob)
        self.hash_count = BloomFilter.get_hash_count(self.size, expected_item_count)
        self.bit_array = bitarray(self.size)
        self.bit_array.setall(False)

    def add(self, item):
        for i in range(self.hash_count):
            bit_position = mmh3.hash(item, i) % self.size
            self.bit_array[bit_position] = True

    def check(self, item):
        for i in range(self.hash_count):
            bit_position = mmh3.hash(item, i) % self.size
            if self.bit_array[bit_position] == False:
                return False
        return True

    @staticmethod
    def get_size( n, p):
        m = -(n * math.log(p))/(math.log(2)**2)
        return int(m)

    @staticmethod
    def get_hash_count( m, n):
        k = (m/n) * math.log(2)
        return int(k)