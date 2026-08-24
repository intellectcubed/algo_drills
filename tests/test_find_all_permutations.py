import os
import importlib
import pytest

ACTIVE_IMPL = os.getenv("ALGO_IMPL", "practice_shells")
if "ALGO_IMPL" not in os.environ:
    print("⚠️  ALGO_IMPL not set — defaulting to 'practice_shells'.")

find_all_module = importlib.import_module(f"{ACTIVE_IMPL}.permutations.find_all")

FindAllPermutations = find_all_module.FindAllPermutations


def test_basic_permutations():
    finder = FindAllPermutations()
    result = finder.permute(['a', 'b', 'c'])
    expected = [
        ['a', 'b', 'c'], ['a', 'c', 'b'],
        ['b', 'a', 'c'], ['b', 'c', 'a'],
        ['c', 'a', 'b'], ['c', 'b', 'a']
    ]
    assert len(result) == 6
    for perm in expected:
        assert perm in result


def test_two_elements():
    finder = FindAllPermutations()
    result = finder.permute(['x', 'y'])
    expected = [['x', 'y'], ['y', 'x']]
    assert len(result) == 2
    for perm in expected:
        assert perm in result


def test_single_element():
    finder = FindAllPermutations()
    result = finder.permute(['a'])
    assert result == [['a']]


def test_empty_list():
    finder = FindAllPermutations()
    result = finder.permute([])
    assert result == []


def test_four_elements():
    finder = FindAllPermutations()
    result = finder.permute([1, 2, 3, 4])
    # 4! = 24 permutations
    assert len(result) == 24
    # Check that all elements are unique
    result_tuples = [tuple(perm) for perm in result]
    assert len(set(result_tuples)) == 24
    # Check that each permutation contains all original elements
    for perm in result:
        assert sorted(perm) == [1, 2, 3, 4]


def test_duplicate_elements():
    finder = FindAllPermutations()
    result = finder.permute(['a', 'a', 'b'])
    # Note: This will generate 3 permutations (3!), excluding duplicates
    assert len(result) == 3
    for perm in result:
        assert sorted(perm) == ['a', 'a', 'b']


def test_numeric_elements():
    finder = FindAllPermutations()
    result = finder.permute([1, 2, 3])
    expected = [
        [1, 2, 3], [1, 3, 2],
        [2, 1, 3], [2, 3, 1],
        [3, 1, 2], [3, 2, 1]
    ]
    assert len(result) == 6
    for perm in expected:
        assert perm in result


def test_mixed_types():
    finder = FindAllPermutations()
    result = finder.permute(['a', 1, 'b'])
    assert len(result) == 6
    for perm in result:
        assert 'a' in perm and 1 in perm and 'b' in perm


def test_multiple_calls():
    finder = FindAllPermutations()
    result1 = finder.permute(['a', 'b'])
    result2 = finder.permute(['x', 'y', 'z'])

    assert len(result1) == 2
    assert len(result2) == 6
    # Ensure the second call doesn't interfere with results
    assert ['a', 'b'] in result1 or ['b', 'a'] in result1
