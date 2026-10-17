<!-- Part of the dev-algorithms-sorting-searching skill. Loaded on demand from SKILL.md. -->

# Searching Algorithms

## Binary Search
- **Precondition**: Array must be sorted.
- **Strategy**: Repeatedly halve the search space by comparing the target to the middle element.
- **Time**: O(log n)
- **Space**: O(1) iterative, O(log n) recursive

```
BINARY_SEARCH(A, target):
    lo = 0, hi = len(A) - 1
    while lo <= hi:
        mid = lo + (hi - lo) / 2
        if A[mid] == target:
            return mid
        else if A[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1  // not found
```

**Variations**: Lower bound (first occurrence), upper bound (last occurrence), search on answer (binary search the solution space).

## Interpolation Search
- **Precondition**: Array must be sorted and values uniformly distributed.
- **Strategy**: Estimate the position of the target based on its value relative to the min and max of the current range.
- **Time**: O(log log n) average for uniformly distributed data, O(n) worst case
- **Best for**: Large, uniformly distributed sorted datasets.

## Two Pointers Technique
- **Strategy**: Use two pointers (indices) that move through the data structure, typically from opposite ends or at different speeds.
- **Time**: Typically O(n)
- **Common applications**: Pair sum in sorted array, removing duplicates, partitioning, palindrome check, merging sorted arrays.

## Sliding Window Technique
- **Strategy**: Maintain a window (contiguous subarray) that slides through the array, expanding or shrinking to satisfy a condition.
- **Time**: Typically O(n)
- **Common applications**: Maximum/minimum subarray of size k, longest substring without repeating characters, smallest subarray with sum >= target.

## Searching Complexity Comparison

| Algorithm | Average | Worst | Precondition |
|-----------|---------|-------|--------------|
| Linear Search | O(n) | O(n) | None |
| Binary Search | O(log n) | O(log n) | Sorted |
| Interpolation Search | O(log log n) | O(n) | Sorted, uniform distribution |
| Hash Lookup | O(1) | O(n) | Hash table built |
| Two Pointers | O(n) | O(n) | Often sorted |
| Sliding Window | O(n) | O(n) | Contiguous subarray problems |
