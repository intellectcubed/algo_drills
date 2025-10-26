from collections import Counter
import heapq

def top_k_frequent_digits(nums, k):
    """
    Return the top k most frequent digits from nums.
    If multiple digits have the same frequency, return smaller digits first.
    """
    if not nums or k <= 0:
        return []

    freq = Counter(nums)
    # Build a max heap with (-frequency, digit) to get highest frequency first
    heap = [(-count, digit) for digit, count in freq.items()]
    heapq.heapify(heap)

    result = []
    while heap and len(result) < k:
        count, digit = heapq.heappop(heap)
        result.append(digit)

    return result
