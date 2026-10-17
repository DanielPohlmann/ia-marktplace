<!-- Part of the dev-algorithms-sorting-searching skill. Loaded on demand from SKILL.md. -->

# Sorting Algorithms

## Comparison Sorts

Comparison-based sorts determine order by comparing pairs of elements. The theoretical lower bound for comparison sorting is O(n log n).

### Quicksort
- **Strategy**: Divide and conquer. Pick a pivot, partition the array so elements less than the pivot come before it and elements greater come after, then recurse.
- **Time**: O(n log n) average, O(n^2) worst case (poor pivot choice)
- **Space**: O(log n) stack space (in-place partitioning)
- **Stable**: No
- **Best for**: General-purpose sorting; fastest in practice for most data distributions due to excellent cache behavior.

```
QUICKSORT(A, lo, hi):
    if lo < hi:
        p = PARTITION(A, lo, hi)
        QUICKSORT(A, lo, p - 1)
        QUICKSORT(A, p + 1, hi)

PARTITION(A, lo, hi):
    pivot = A[hi]
    i = lo - 1
    for j = lo to hi - 1:
        if A[j] <= pivot:
            i = i + 1
            swap A[i] and A[j]
    swap A[i + 1] and A[hi]
    return i + 1
```

### Mergesort
- **Strategy**: Divide and conquer. Split the array in half, recursively sort each half, then merge the two sorted halves.
- **Time**: O(n log n) in all cases
- **Space**: O(n) auxiliary
- **Stable**: Yes
- **Best for**: When stability is required, linked lists, external sorting (large files that do not fit in memory).

```
MERGESORT(A, lo, hi):
    if lo < hi:
        mid = (lo + hi) / 2
        MERGESORT(A, lo, mid)
        MERGESORT(A, mid + 1, hi)
        MERGE(A, lo, mid, hi)

MERGE(A, lo, mid, hi):
    create temporary arrays L = A[lo..mid], R = A[mid+1..hi]
    i = 0, j = 0, k = lo
    while i < |L| and j < |R|:
        if L[i] <= R[j]:
            A[k] = L[i]; i++
        else:
            A[k] = R[j]; j++
        k++
    copy remaining elements of L or R into A
```

### Heapsort
- **Strategy**: Build a max-heap from the array, then repeatedly extract the maximum to build the sorted result.
- **Time**: O(n log n) in all cases
- **Space**: O(1) (in-place)
- **Stable**: No
- **Best for**: When guaranteed O(n log n) is needed without extra memory. Not cache-friendly, so often slower than Quicksort in practice.

### Insertion Sort
- **Strategy**: Build the sorted array one element at a time by inserting each element into its correct position among the already-sorted elements.
- **Time**: O(n) best case (nearly sorted), O(n^2) worst/average case
- **Space**: O(1) (in-place)
- **Stable**: Yes
- **Best for**: Small arrays, nearly sorted data, online sorting (data arrives one element at a time). Often used as the base case in hybrid sorts.

### Timsort
- **Strategy**: Hybrid of Mergesort and Insertion sort. Identifies natural runs (already sorted subsequences), extends them with insertion sort, then merges runs using an optimized merge procedure.
- **Time**: O(n) best case (already sorted), O(n log n) worst case
- **Space**: O(n) auxiliary
- **Stable**: Yes
- **Best for**: Real-world data that often contains partially sorted subsequences. Default sort in Python and Java.

## Linear Sorts

These sorts exploit constraints on the input (bounded range, integer keys) to beat the O(n log n) comparison lower bound.

### Counting Sort
- **Strategy**: Count occurrences of each value, then compute positions from cumulative counts.
- **Time**: O(n + k) where k is the range of input values
- **Space**: O(n + k)
- **Stable**: Yes
- **Best for**: Small integer ranges (e.g., sorting grades 0-100, characters).

### Radix Sort
- **Strategy**: Sort by each digit/character position from least significant to most significant, using a stable sub-sort (typically counting sort) at each position.
- **Time**: O(d * (n + k)) where d is the number of digits and k is the radix
- **Space**: O(n + k)
- **Stable**: Yes
- **Best for**: Fixed-length integers or strings with bounded alphabet.

### Bucket Sort
- **Strategy**: Distribute elements into buckets based on value range, sort each bucket individually, then concatenate.
- **Time**: O(n + k) average when input is uniformly distributed; O(n^2) worst case
- **Space**: O(n + k)
- **Stable**: Depends on bucket sort
- **Best for**: Uniformly distributed floating-point numbers in a known range.

## Sorting Complexity Comparison

| Algorithm | Best | Average | Worst | Space | Stable |
|-----------|------|---------|-------|-------|--------|
| Quicksort | O(n log n) | O(n log n) | O(n^2) | O(log n) | No |
| Mergesort | O(n log n) | O(n log n) | O(n log n) | O(n) | Yes |
| Heapsort | O(n log n) | O(n log n) | O(n log n) | O(1) | No |
| Insertion Sort | O(n) | O(n^2) | O(n^2) | O(1) | Yes |
| Timsort | O(n) | O(n log n) | O(n log n) | O(n) | Yes |
| Counting Sort | O(n + k) | O(n + k) | O(n + k) | O(n + k) | Yes |
| Radix Sort | O(d(n + k)) | O(d(n + k)) | O(d(n + k)) | O(n + k) | Yes |
| Bucket Sort | O(n + k) | O(n + k) | O(n^2) | O(n + k) | Varies |

## When to Use Which Sort

| Situation | Recommended Sort |
|-----------|-----------------|
| General purpose, in-memory | Quicksort (or language default, often Timsort) |
| Stability required | Mergesort or Timsort |
| Guaranteed O(n log n), no extra space | Heapsort |
| Small arrays (n < 20) | Insertion Sort |
| Nearly sorted data | Insertion Sort or Timsort |
| Integer keys with small range | Counting Sort |
| Fixed-length integer/string keys | Radix Sort |
| Uniformly distributed floating-point data | Bucket Sort |
| External sorting (data on disk) | External Mergesort |
| Linked list sorting | Mergesort |
