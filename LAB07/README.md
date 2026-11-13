# Lab 7 – Fuzz Testing: Customs Duty Calculator

## 1. Overview

This lab demonstrates **fuzz testing** using Python's `Hypothesis` library and conventional test cases using `pytest`.

The Customs Duty Calculator contains three functions that process customs declaration data:

- `parse_declaration()` – Parses a category and declared value.
- `duty_amount()` – Calculates customs duty using a value and duty rate.
- `hs_chapter()` – Extracts the first two digits of an HS code to identify its chapter.

The objective is to test these functions with both valid and unexpected inputs, identify potential failures, and improve input validation.

## 2. Project Structure

```text
LAB07/
├── README.md
├── customs_duty.py
└── test_customs_duty.py
```

| File | Description |
|---|---|
| `customs_duty.py` | Contains the customs duty calculation and parsing functions. |
| `test_customs_duty.py` | Contains Hypothesis-based fuzz tests and regular pytest test cases. |
| `README.md` | Documents the lab, implementation, and testing process. |

## 3. Functions Under Test

### `parse_declaration(text)`

Accepts a declaration in the format `category:value`.

Example:
```python
parse_declaration("electronics:25000")
```

Expected output:
```python
("electronics", 25000.0)
```

### `duty_amount(text)`

Calculates customs duty from an input in the format `value@rate`.

Example:
```python
duty_amount("25000@20")
```

Expected output:
```python
5000.0
```

### `hs_chapter(code)`

Extracts the first two digits of an HS code.

Example:
```python
hs_chapter("8517.12")
```

Expected output:
```python
85
```

## 4. Input Validation

The functions validate inputs before processing them.

The implementation checks for:

- Incorrect input types.
- Missing or extra separators.
- Empty categories.
- Non-numeric values.
- Negative or non-finite numerical values.
- Invalid HS code formats.

Invalid inputs are rejected using `ValueError` with an explanatory message.

## 5. Fuzz Testing with Hypothesis

Fuzz testing supplies functions with a wide variety of generated inputs to discover unexpected failures.

The tests use:

```python
from hypothesis import given, strategies as st
```

The following strategy generates arbitrary strings and `None` values:

```python
st.text() | st.none()
```

Three fuzz tests are implemented:

| Test | Function tested | Input generated |
|---|---|---|
| `test_parse_declaration_no_crash` | `parse_declaration()` | Arbitrary strings and `None` |
| `test_duty_amount_no_crash` | `duty_amount()` | Arbitrary strings and `None` |
| `test_hs_chapter_no_crash` | `hs_chapter()` | Arbitrary strings and `None` |

The tests allow expected `ValueError` exceptions for malformed inputs. Unexpected exceptions cause the tests to fail.

## 6. Additional Test Cases

Along with fuzz testing, pytest is used to verify:

- Valid input and expected output.
- Empty input.
- Missing separators.
- Invalid numeric values.
- Invalid HS codes.
- `None` input.

Parameterized tests are used to check multiple invalid inputs efficiently.

## 7. Installation and Execution

Install the required dependencies:

```bash
python -m pip install pytest hypothesis
```

Run all tests:

```bash
python -m pytest -v
```

Run tests with Hypothesis statistics:

```bash
python -m pytest -v --hypothesis-show-statistics
```

## 8. Test Results

The test suite was executed successfully.

**Result: 20 passed in 2.21 seconds.**

The test run included:

- 3 Hypothesis fuzz tests.
- 3 valid-input tests.
- 14 invalid-input test cases.

All 20 tests passed without failures.

## 9. Conclusion

Fuzz testing was performed on the Customs Duty Calculator using Hypothesis. The functions were tested against automatically generated inputs, including malformed strings and `None` values.

Input validation was added to handle invalid declarations, duty calculations, and HS codes safely. Additional pytest cases verified expected outputs and error handling.

The successful test run demonstrates that the tested functions handle the generated inputs and defined test cases as expected.
