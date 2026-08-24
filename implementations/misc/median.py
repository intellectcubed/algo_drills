import heapq
from collections import defaultdict


class Container:
    """
    A container supporting add, delete, and get_median operations.

    Uses two heaps:
    - max_heap (lower half): stored as negated values since Python only has min-heap
    - min_heap (upper half): stores values as-is

    Invariant: len(max_heap) == len(min_heap) or len(max_heap) == len(min_heap) + 1
    (where lengths account for lazy-deleted elements)
    """

    def __init__(self):
        self.max_heap = []  # lower half (negated values)
        self.min_heap = []  # upper half
        self.deleted = defaultdict(int)  # lazy deletion counts
        self.max_heap_size = 0  # effective size (excludes deleted)
        self.min_heap_size = 0

    def add(self, value: int) -> None:
        """
        Adds the specified value to the container

        :param value: int
        """
        # Add to max_heap first
        heapq.heappush(self.max_heap, -value)
        self.max_heap_size += 1

        # Rebalance: move top of max_heap to min_heap
        self._prune(self.max_heap, negate=True)
        if self.max_heap:
            val = -heapq.heappop(self.max_heap)
            self.max_heap_size -= 1
            heapq.heappush(self.min_heap, val)
            self.min_heap_size += 1

        # Rebalance: ensure max_heap has >= elements than min_heap
        self._prune(self.min_heap, negate=False)
        if self.max_heap_size < self.min_heap_size:
            val = heapq.heappop(self.min_heap)
            self.min_heap_size -= 1
            heapq.heappush(self.max_heap, -val)
            self.max_heap_size += 1

    def delete(self, value: int) -> bool:
        """
        Attempts to delete one item of the specified value from the container

        :param value: int
        :return: True, if the value has been deleted, or
                 False, otherwise.
        """
        # Check which heap the value belongs to
        self._prune(self.max_heap, negate=True)
        self._prune(self.min_heap, negate=False)

        if self.max_heap_size == 0 and self.min_heap_size == 0:
            return False

        # Determine which heap the value is in based on median
        median = self._get_median_value()

        if value <= median:
            # Should be in max_heap
            if not self._contains(self.max_heap, -value, negate=True, target=value):
                return False
            self.deleted[value] += 1
            self.max_heap_size -= 1
        else:
            # Should be in min_heap
            if not self._contains(self.min_heap, value, negate=False, target=value):
                return False
            self.deleted[value] += 1
            self.min_heap_size -= 1

        # Rebalance if needed
        self._rebalance()
        return True

    def _contains(self, heap, heap_value, negate, target):
        """Check if target value exists in heap (accounting for deletions)."""
        count = 0
        for v in heap:
            actual = -v if negate else v
            if actual == target:
                count += 1
        return count > self.deleted.get(target, 0)

    def _rebalance(self):
        """Ensure the heap size invariant is maintained."""
        self._prune(self.max_heap, negate=True)
        self._prune(self.min_heap, negate=False)

        # max_heap should have same size or one more than min_heap
        while self.max_heap_size > self.min_heap_size + 1:
            self._prune(self.max_heap, negate=True)
            val = -heapq.heappop(self.max_heap)
            self.max_heap_size -= 1
            heapq.heappush(self.min_heap, val)
            self.min_heap_size += 1
            self._prune(self.max_heap, negate=True)

        while self.min_heap_size > self.max_heap_size:
            self._prune(self.min_heap, negate=False)
            val = heapq.heappop(self.min_heap)
            self.min_heap_size -= 1
            heapq.heappush(self.max_heap, -val)
            self.max_heap_size += 1
            self._prune(self.min_heap, negate=False)

    def _prune(self, heap, negate):
        """Remove lazy-deleted elements from top of heap."""
        while heap:
            val = -heap[0] if negate else heap[0]
            if self.deleted.get(val, 0) > 0:
                heapq.heappop(heap)
                self.deleted[val] -= 1
                if self.deleted[val] == 0:
                    del self.deleted[val]
            else:
                break

    def _get_median_value(self):
        """Get median without the empty check."""
        self._prune(self.max_heap, negate=True)
        return -self.max_heap[0]

    def get_median(self) -> int:
        """
        Finds the container's median integer value, which is
        the middle integer when the all integers are sorted in order.
        If the sorted array has an even length,
        the leftmost integer between the two middle
        integers should be considered as the median.

        :return: The median if the array is not empty, or
        :raise:  a runtime exception, otherwise.
        """
        if self.max_heap_size == 0 and self.min_heap_size == 0:
            raise RuntimeError("Container is empty")

        self._prune(self.max_heap, negate=True)
        return -self.max_heap[0]