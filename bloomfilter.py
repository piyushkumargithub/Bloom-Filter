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

    def add(self, item: str) -> None:
        '''
        Add an item to the Bloom filter
        '''
        for i in range(self.hash_count):
            bit_position = mmh3.hash(item, i) % self.size
            self.bit_array[bit_position] = True

    def check(self, item: str) -> bool:
        '''
        Check if the item is present in the Bloom filter or not
        '''
        for i in range(self.hash_count):
            bit_position = mmh3.hash(item, i) % self.size
            if self.bit_array[bit_position] == False:
                return False
        return True

    @staticmethod
    def get_size(expected_item_count: int, fp_prob: float) -> int:
        '''
        Calculate the size of the bit array
        '''
        size = -(expected_item_count * math.log(fp_prob)) / (math.log(2) ** 2)
        return int(size)

    @staticmethod
    def get_hash_count(bit_array_size: int, expected_item_count: int) -> int:
        '''
        Calculate the optimal number of hash functions
        '''
        hash_count = (bit_array_size / expected_item_count) * math.log(2)
        return int(hash_count)
    
class CountingBloomFilter(object):
    def __init__(self, expected_item_count: int, fp_prob: float):
        '''
        expected_item_count: Number of items expected to be stored in the filter
        
        fp_prob: False Positive probability
        '''
        self.fp_prob = fp_prob
        self.size = BloomFilter.get_size(expected_item_count, fp_prob)
        self.hash_count = BloomFilter.get_hash_count(self.size, expected_item_count)
        self.bit_array = [0] * self.size

    def add(self, item: str) -> None:
        '''
        Add an item to the Bloom filter
        '''
        for i in range(self.hash_count):
            bit_position = mmh3.hash(item, i) % self.size
            self.bit_array[bit_position] += 1

    def delete(self, item: str) -> None:
        '''
        Delete an item from the Bloom filter
        '''
        for i in range(self.hash_count):
            bit_position = mmh3.hash(item, i) % self.size
            if self.bit_array[bit_position] > 0:
                self.bit_array[bit_position] -= 1
    def check(self, item: str) -> bool:
        '''
        Check if the item is present in the Bloom filter or not
        '''
        for i in range(self.hash_count):
            bit_position = mmh3.hash(item, i) % self.size
            if self.bit_array[bit_position] == 0:
                return False
        return True