from typing import List


def compute_divisor_counts(limit: int) -> List[int]:
    """
    Computes the number of divisors for every number up to 'limit'
    using a sieve-like approach.
    """
    divisor_counts = [0] * (limit + 1)

    for divisor in range(1, limit + 1):
        for multiple in range(divisor, limit + 1, divisor):
            divisor_counts[multiple] += 1

    return divisor_counts


def build_prefix_equal_divisor_counts(divisor_counts: List[int]) -> List[int]:
    """
    Builds a prefix array where prefix[i] stores the count of numbers n
    (2 ≤ n ≤ i) such that:
        divisor_counts[n] == divisor_counts[n + 1]
    """
    limit = len(divisor_counts) - 1
    prefix_counts = [0] * (limit + 1)

    for number in range(2, limit):
        prefix_counts[number] = prefix_counts[number - 1]

        if divisor_counts[number] == divisor_counts[number + 1]:
            prefix_counts[number] += 1

    return prefix_counts


def count_valid_numbers(limit: int, prefix_counts: List[int]) -> int:
    """
    Returns the number of valid n such that:
        1 < n < limit
        d(n) == d(n + 1)
    """
    if limit <= 2:
        return 0

    return prefix_counts[limit - 1]


def process_test_cases(test_cases: List[int]) -> List[int]:
    """
    Processes all test cases efficiently using precomputation.
    """
    if not test_cases:
        return []

    max_limit = max(test_cases)

    divisor_counts = compute_divisor_counts(max_limit)
    prefix_counts = build_prefix_equal_divisor_counts(divisor_counts)

    return [count_valid_numbers(limit, prefix_counts) for limit in test_cases]


def read_input() -> List[int]:
    """
    Reads input from stdin and returns list of test cases.
    """
    test_case_count = int(input().strip())
    return [int(input().strip()) for _ in range(test_case_count)]


def print_results(results: List[int]) -> None:
    """
    Prints results to stdout.
    """
    for result in results:
        print(result)


def main():
    """
    Entry point of the application.
    """
    try:
        test_cases = read_input()
        results = process_test_cases(test_cases)
        print_results(results)

    except ValueError:
        print("Invalid input")


if __name__ == "__main__":
    main()
