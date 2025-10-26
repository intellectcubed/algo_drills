import os
import importlib
import random
from collections import Counter

ACTIVE_IMPL = os.getenv("ALGO_IMPL", "practice_shells")
if "ALGO_IMPL" not in os.environ:
    print("⚠️  ALGO_IMPL not set — defaulting to 'practice_shells'.")

top_k_module = importlib.import_module(f"{ACTIVE_IMPL}.heaps.top_k_frequent_digits")
top_k_frequent_digits = top_k_module.top_k_frequent_digits


def test_typical_case():
    nums = [1, 1, 2, 2, 2, 3]
    k = 2
    assert top_k_frequent_digits(nums, k) == [2, 1]


def test_with_ties():
    nums = [4, 4, 5, 5, 6]
    k = 2
    # 4 and 5 tie, 4 < 5 → [4, 5]
    assert top_k_frequent_digits(nums, k) == [4, 5]


def test_k_larger_than_unique():
    nums = [7, 7, 8]
    k = 5
    assert top_k_frequent_digits(nums, k) == [7, 8]


def test_empty_input():
    assert top_k_frequent_digits([], 3) == []


def test_k_zero():
    assert top_k_frequent_digits([1, 2, 3], 0) == []


def test_all_same_digit():
    assert top_k_frequent_digits([9, 9, 9, 9], 1) == [9]


def test_performance_large_input():
    """
    Test performance with large random input.
    Ensures function handles ~100,000 digits efficiently.
    """
    random.seed(42)
    nums = [random.randint(0, 9) for _ in range(100_000)]
    k = 5

    result = top_k_frequent_digits(nums, k)
    assert isinstance(result, list)
    assert len(result) <= k

    # Validate output matches expected top frequencies
    freq = Counter(nums)
    expected = sorted(freq.items(), key=lambda x: (-x[1], x[0]))[:k]
    expected
