# 📊 Consecutive Equal Divisors Counter

## 🧩 Problem Statement

Given an integer `k`, count how many integers `n` exist such that:

* ( 1 < n < k )
* The number of positive divisors of `n` is equal to the number of positive divisors of `n + 1`

### 🔍 Definition: Positive Divisors

A positive divisor of a number is a number that divides it completely.

**Example:**

* Divisors of 14 → `1, 2, 7, 14`

---

## 📥 Input Format

* First line: Integer `t` (number of test cases)
* Next `t` lines: Each contains an integer `k`

---

## 📤 Output Format

* For each test case, output a single integer representing the count of valid `n`

---

## ✅ Example

### Input

```
1
15
```

### Output

```
2
```

### Explanation

Valid values:

* `n = 2` → (2, 3)
* `n = 14` → (14, 15)

---

## 🚀 Approach & Optimization

### 🧠 Strategy

Instead of recalculating divisors for each number:

1. Use a **sieve-like approach** to compute divisor counts for all numbers up to `max(k)`
2. Build a **prefix array** to store counts of valid `n`
3. Answer each test case in **O(1)** time

---

### ⚡ Complexity

| Step                | Complexity |
| ------------------- | ---------- |
| Divisor computation | O(n log n) |
| Prefix array build  | O(n)       |
| Each query          | O(1)       |

---

## 🏗️ Project Structure

```
project/
│
├── consecutive_divisors_counter.py   # Main solution
├── test_consecutive_divisors_counter.py  # Unit tests
├── README.md
└── requirements.txt
```

---

## ▶️ How to Run

### 🔹 Run the Application

```
python consecutive_divisors_counter.py
```

Then provide input:

```
1
15
```

---

### 🧪 Run Tests

Make sure pytest is installed:

```
pip install pytest
```

Run tests:

```
pytest
```

---

## 🧪 Test Coverage

The test suite includes:

### ✅ Positive Cases

* Example inputs
* Small and medium values

### ⚠️ Edge Cases

* `k = 0, 1, 2`

### ❌ Negative Cases

* Invalid input types
* Empty test cases

---

## 🧼 Clean Code Principles Applied

* ✅ Meaningful function names
* ✅ Single Responsibility Principle
* ✅ Separation of concerns (input, logic, output)
* ✅ DRY (no repeated computation)
* ✅ Modular and testable design

---

## 🧪 TDD Approach

* Tests written to validate:

  * Correctness
  * Edge conditions
  * Input validation
* Code structured to support easy testing and maintainability

---

## 📌 Key Functions

* `compute_divisor_counts(limit)`
* `build_prefix_equal_divisor_counts(divisor_counts)`
* `count_valid_numbers(limit, prefix_counts)`
* `process_test_cases(test_cases)`

---

## 💡 Future Improvements

* Optimize further for very large constraints (≥ 10⁷)
* Add benchmarking and performance tests
* Integrate CI/CD pipeline for automated testing
