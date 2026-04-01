import pytest
from consecutive_divisors_counter import (
    process_test_cases,
    compute_divisor_counts,
    build_prefix_equal_divisor_counts,
    count_valid_numbers,
)


def prepare_prefix(limit: int):
    """
    Helper function to prepare prefix counts for testing.
    """
    divisor_counts = compute_divisor_counts(limit)
    return build_prefix_equal_divisor_counts(divisor_counts)



def test_given_example():
    prefix = prepare_prefix(15)
    assert count_valid_numbers(15, prefix) == 2


def test_small_input():
    prefix = prepare_prefix(3)
    assert count_valid_numbers(3, prefix) == 0


def test_medium_input_returns_integer():
    prefix = prepare_prefix(50)
    result = count_valid_numbers(50, prefix)
    assert isinstance(result, int)


def test_multiple_test_cases():
    test_cases = [3, 15, 20]
    results = process_test_cases(test_cases)

    assert isinstance(results, list)
    assert len(results) == len(test_cases)



def test_zero_input():
    prefix = prepare_prefix(2)
    assert count_valid_numbers(0, prefix) == 0


def test_one_input():
    prefix = prepare_prefix(2)
    assert count_valid_numbers(1, prefix) == 0


def test_two_input():
    prefix = prepare_prefix(2)
    assert count_valid_numbers(2, prefix) == 0



def test_invalid_type_input():
    with pytest.raises(TypeError):
        count_valid_numbers("10", [])  


def test_empty_test_cases():
    assert process_test_cases([]) == []
