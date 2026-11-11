# Lab 6 – Code and Branch Coverage Analysis

## Project
Customs Duty Application

## Initial Coverage
- Line coverage: 36%
- Branch coverage: 31%

## Final Coverage
- Line coverage: 100% (36/36 statements)
- Branch coverage: 100% (28/28 branches)
- Partial branches: 0

## Test Results
- Code coverage suite: 18 tests passed
- Branch coverage suite: 28 tests passed

## Commands Used

### Code Coverage
coverage erase
coverage run --include="customs_duty.py" -m pytest -v CodeCoverageTest_411_application.py
coverage report -m

### Branch Coverage
coverage erase
coverage run --branch --include="customs_duty.py" -m pytest -v BranchCoverageTest_411_application.py
coverage report -m

## Conclusion
The final test suites achieved 100% statement coverage and
100% branch coverage for customs_duty.py.
