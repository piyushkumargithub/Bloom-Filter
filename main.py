from bloomfilter import BloomFilter, CountingBloomFilter
from random import shuffle

n = 20 #no of items to add
p = 0.005 #false positive probability

bloomf = BloomFilter(n,p)
print("Size of bit array:{}".format(bloomf.size))
print("False positive Probability:{}".format(bloomf.fp_prob))
print("Number of hash functions:{}".format(bloomf.hash_count))

word_present = ['abound','abounds','abundance','abundant','accessable',
                'bloom','blossom','bolster','bonny','bonus','bonuses',
                'coherent','cohesive','colorful','comely','comfort',
                'gems','generosity','generous','generously','good']

for item in word_present:
    bloomf.add(item)

print(bloomf.check('somedifferentword')) 

countingbloomf = CountingBloomFilter(n,p)

for item in word_present:
    countingbloomf.add(item)
print(countingbloomf.check('somedifferentword'))

print(countingbloomf.check('abound'))
countingbloomf.delete('abound')
print(countingbloomf.check('abound'))