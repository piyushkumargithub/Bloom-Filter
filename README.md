# Bloom Filter Implementation in Python

This repository contains a Python implementation of a Bloom Filter, a probabilistic data structure that provides fast membership tests with a configurable false positive probability. The implementation uses the Murmur3 hash function and the `bitarray` library.

## Why This Repository?
I created this repository to make the Bloom Filter concept more understandable and the implementation as clear and efficient as possible. The code avoids unnecessary complexities and emphasizes clean, maintainable practices, such as using static methods for utility functions and choosing clear variable names.

## Key Features
- **Simple and Clean Code:** Readable code with meaningful variable names and concise methods.
- **Optimized Performance:** Avoids unnecessary data structures and computations.
- **Educational Value:** Great for those looking to learn about Bloom Filters and hash-based data structures.

## How It Works
A Bloom Filter uses multiple hash functions to map input items to a bit array. When an item is added, it sets specific bits to `True`. To check if an item might be present, the filter verifies the same bits. If all relevant bits are `True`, the item is probably present (with a configurable false positive rate). If any bit is `False`, the item is definitely not present.

### Example Usage
```python
from bloom_filter import BloomFilter

# Initialize Bloom Filter with expected item count and false positive probability
bloom = BloomFilter(expected_item_count=20, fp_prob=0.05)

# Add items to the Bloom Filter
bloom.add("apple")
bloom.add("banana")

# Check for existence of items
print(bloom.check("apple"))  # Output: True
print(bloom.check("grape"))  # Output: False (probably)
```

## Installation
```bash
pip install mmh3
pip install bitarray
```


---
Feel free to explore, learn, and contribute!

