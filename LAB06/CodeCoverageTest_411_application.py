import pytest

from customs_duty import duty_rate, total_duty, clearance_channel


# ==========================================
# 1. DUTY RATE TESTS
# ==========================================

def test_prohibited_item():
    with pytest.raises(ValueError, match="prohibited item"):
        duty_rate("weapons", "US")


@pytest.mark.parametrize("category, origin, expected", [
    ("electronics", "FTA", 0.10),
    ("electronics", "US", 0.20),
    ("clothing", "FTA", 0.05),
    ("clothing", "US", 0.12),
    ("books", "US", 0),
    ("furniture", "US", 0.15),
])
def test_duty_rate_categories(category, origin, expected):
    assert duty_rate(category, origin) == expected
