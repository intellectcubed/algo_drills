import importlib
import os
import pytest

ACTIVE_IMPLEMENTATION = os.getenv("ALGO_IMPL", "practice_shells")
if "ALGO_IMPL" not in os.environ:
    print("⚠️  ALGO_IMPL not set — defaulting to 'practice_shells'.")

Container = importlib.import_module(f"{ACTIVE_IMPLEMENTATION}.misc.median").Container


def test_single_element():
    c = Container()
    c.add(5)
    assert c.get_median() == 5


def test_two_elements():
    c = Container()
    c.add(5)
    c.add(10)
    # With even count, median is leftmost of the two middle elements
    assert c.get_median() == 5


def test_three_elements():
    c = Container()
    c.add(5)
    c.add(10)
    c.add(3)
    # Sorted: [3, 5, 10], median is 5
    assert c.get_median() == 5


def test_four_elements():
    c = Container()
    c.add(1)
    c.add(2)
    c.add(3)
    c.add(4)
    # Sorted: [1, 2, 3, 4], even length, median is leftmost middle = 2
    assert c.get_median() == 2


def test_five_elements():
    c = Container()
    c.add(1)
    c.add(2)
    c.add(3)
    c.add(4)
    c.add(5)
    # Sorted: [1, 2, 3, 4, 5], median is 3
    assert c.get_median() == 3


def test_duplicates():
    c = Container()
    c.add(5)
    c.add(5)
    c.add(5)
    assert c.get_median() == 5


def test_negative_numbers():
    c = Container()
    c.add(-5)
    c.add(-10)
    c.add(-3)
    # Sorted: [-10, -5, -3], median is -5
    assert c.get_median() == -5


def test_mixed_positive_negative():
    c = Container()
    c.add(-5)
    c.add(0)
    c.add(5)
    # Sorted: [-5, 0, 5], median is 0
    assert c.get_median() == 0


def test_delete_returns_true_when_found():
    c = Container()
    c.add(5)
    c.add(10)
    assert c.delete(5) == True


def test_delete_returns_false_when_not_found():
    c = Container()
    c.add(5)
    assert c.delete(10) == False


def test_delete_from_empty():
    c = Container()
    assert c.delete(5) == False


def test_delete_updates_median():
    c = Container()
    c.add(1)
    c.add(2)
    c.add(3)
    # Sorted: [1, 2, 3], median is 2
    assert c.get_median() == 2
    c.delete(1)
    # Sorted: [2, 3], median is 2 (leftmost of middle two)
    assert c.get_median() == 2


def test_delete_only_one_duplicate():
    c = Container()
    c.add(5)
    c.add(5)
    c.add(5)
    assert c.delete(5) == True
    # Still has two 5s
    assert c.get_median() == 5
    assert c.delete(5) == True
    # Still has one 5
    assert c.get_median() == 5
    assert c.delete(5) == True
    # Now empty


def test_get_median_empty_raises():
    c = Container()
    with pytest.raises(Exception):
        c.get_median()


def test_add_after_delete():
    c = Container()
    c.add(1)
    c.add(2)
    c.add(3)
    c.delete(2)
    # Sorted: [1, 3], median is 1
    assert c.get_median() == 1
    c.add(4)
    # Sorted: [1, 3, 4], median is 3
    assert c.get_median() == 3


def test_large_sequence():
    c = Container()
    for i in range(1, 101):
        c.add(i)
    # Sorted: [1, 2, ..., 100], even count, median is 50
    assert c.get_median() == 50


def test_reverse_insertion():
    c = Container()
    for i in range(10, 0, -1):
        c.add(i)
    # Sorted: [1, 2, ..., 10], median is 5
    assert c.get_median() == 5


def test_delete_median():
    c = Container()
    c.add(1)
    c.add(2)
    c.add(3)
    c.add(4)
    c.add(5)
    # Median is 3
    assert c.get_median() == 3
    c.delete(3)
    # Sorted: [1, 2, 4, 5], median is 2
    assert c.get_median() == 2


def test_multiple_duplicates_with_delete():
    """User's example: add(4) x4, add(5), delete(4) x2"""
    c = Container()
    c.add(4)
    c.add(4)
    c.add(4)
    c.add(4)
    c.add(5)
    # Sorted: [4, 4, 4, 4, 5], median is 4
    assert c.get_median() == 4
    c.delete(4)
    # Sorted: [4, 4, 4, 5], median is 4 (leftmost of middle two)
    assert c.get_median() == 4
    c.delete(4)
    # Sorted: [4, 4, 5], median is 4
    assert c.get_median() == 4


def test_duplicates_spanning_both_heaps():
    """Duplicates that end up in both lower and upper heaps"""
    c = Container()
    c.add(5)
    c.add(5)
    c.add(5)
    c.add(5)
    c.add(5)
    # Sorted: [5, 5, 5, 5, 5], median is 5
    assert c.get_median() == 5
    c.delete(5)
    c.delete(5)
    # Sorted: [5, 5, 5], median is 5
    assert c.get_median() == 5
    c.add(3)
    c.add(7)
    # Sorted: [3, 5, 5, 5, 7], median is 5
    assert c.get_median() == 5


def test_delete_all_duplicates_then_add():
    """Delete all instances of a duplicate, then add new values"""
    c = Container()
    c.add(3)
    c.add(3)
    c.add(3)
    c.delete(3)
    c.delete(3)
    c.delete(3)
    # Now empty
    c.add(1)
    c.add(2)
    # Sorted: [1, 2], median is 1
    assert c.get_median() == 1


def test_duplicates_delete_nonexistent_after_all_removed():
    """Try to delete a value after all instances are removed"""
    c = Container()
    c.add(5)
    c.add(5)
    assert c.delete(5) == True
    assert c.delete(5) == True
    assert c.delete(5) == False  # No more 5s


def test_many_duplicates_interleaved_operations():
    """Complex sequence of adds and deletes with duplicates"""
    c = Container()
    # Add [1, 1, 1, 2, 2, 3]
    c.add(1)
    c.add(2)
    c.add(1)
    c.add(3)
    c.add(2)
    c.add(1)
    # Sorted: [1, 1, 1, 2, 2, 3], median is 1 (leftmost middle)
    assert c.get_median() == 1

    c.delete(1)
    # Sorted: [1, 1, 2, 2, 3], median is 2
    assert c.get_median() == 2

    c.delete(2)
    # Sorted: [1, 1, 2, 3], median is 1
    assert c.get_median() == 1

    c.add(1)
    # Sorted: [1, 1, 1, 2, 3], median is 1
    assert c.get_median() == 1


def test_duplicates_at_median_boundary():
    """Duplicates right at the median position"""
    c = Container()
    c.add(1)
    c.add(2)
    c.add(2)
    c.add(2)
    c.add(3)
    # Sorted: [1, 2, 2, 2, 3], median is 2
    assert c.get_median() == 2

    c.delete(2)
    # Sorted: [1, 2, 2, 3], median is 2
    assert c.get_median() == 2

    c.delete(2)
    # Sorted: [1, 2, 3], median is 2
    assert c.get_median() == 2

    c.delete(2)
    # Sorted: [1, 3], median is 1
    assert c.get_median() == 1


def test_large_duplicate_count():
    """Many instances of the same value"""
    c = Container()
    for _ in range(100):
        c.add(42)
    assert c.get_median() == 42

    for _ in range(50):
        c.delete(42)
    assert c.get_median() == 42

    c.add(1)
    # Sorted: [1, 42, 42, ..., 42] (51 elements), median is 42
    assert c.get_median() == 42

    c.add(100)
    # Sorted: [1, 42, 42, ..., 42, 100] (52 elements), median is 42
    assert c.get_median() == 42
