# Counting Bloom Filter

A Counting Bloom Filter is a probabilistic data structure used for approximate set membership tests, supporting both insertion and deletion operations. Unlike the standard Bloom Filter, which only uses a bit array, the Counting Bloom Filter maintains an array of counters to keep track of how many elements contribute to each bit being set. This additional information allows for safe deletions.

## Problem Statement

In a standard Bloom Filter, deletion is not possible because clearing a bit might also affect other elements that contributed to that bit being set. The Counting Bloom Filter solves this by using counters instead of simple bits, allowing safe decrementing when deleting an item.

However, an issue arises when attempting to delete a non-existent element. The false positive nature of the filter may lead to erroneously decrementing counters that belong to existing items, potentially causing them to vanish incorrectly. For example, if an item `A` and a non-existent item `C` both hash to the same counter, and `C` is deleted, the counter might be decremented, impacting the presence of `A`.

## How It Works

1. **Insertion:** When an item is added, the filter increments the relevant counters based on its hash functions.
2. **Deletion:** When an item is deleted, the counters are decremented. The counters are only decremented if they are greater than 0, but this still does not fully eliminate the risk of false negatives.
3. **Checking:** An item is considered to exist if all relevant counters are greater than 0.

## Usage
```python
# Example usage of Counting Bloom Filter
cbf = CountingBloomFilter(expected_item_count=100, fp_prob=0.01)
cbf.add("apple")
print(cbf.check("apple"))  # Should return True
cbf.delete("apple")
print(cbf.check("apple"))  # Should return False
```

## Limitations
- **False Positives:** Like a standard Bloom Filter, the Counting Bloom Filter can still give false positives, leading to potential mismanagement of the counters during deletions.
- **Risk of False Negatives:** Deleting a non-existent item can lead to decremented counters, possibly causing existing items to be lost if they share hash indices.

## Possible Solution
To avoid this issue, a more advanced data structure like a **Cuckoo Filter** might be more suitable, as it directly manages individual elements and avoids the decrementing problem associated with false positives in Counting Bloom Filters.


