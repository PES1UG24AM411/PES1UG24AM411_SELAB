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


# ==========================================
# 2. TOTAL DUTY TESTS
# ==========================================

def test_negative_value():
    with pytest.raises(ValueError, match="negative value"):
        total_duty("electronics", -100, "US", False)


def test_low_value_gift():
    assert total_duty("electronics", 4000, "US", True) == 0


def test_gift_above_exemption():
    assert total_duty("electronics", 6000, "FTA", True) == 100


def test_minimum_duty_for_gift():
    assert total_duty("clothing", 5500, "FTA", True) == 50


def test_low_value_non_gift():
    assert total_duty("electronics", 1000, "US", False) == 0


def test_normal_duty_calculation():
    assert total_duty("electronics", 2000, "FTA", False) == 200


def test_zero_duty():
    assert total_duty("books", 2000, "US", False) == 0


# ==========================================
# 3. CLEARANCE CHANNEL TESTS
# ==========================================

def test_prohibited_item_refused():
    assert clearance_channel(500, "weapons", True) == "refuse"


def test_high_value_item_inspected():
    assert clearance_channel(150000, "electronics", True) == "inspect"


def test_missing_documents_inspected():
    assert clearance_channel(30000, "electronics", False) == "inspect"


def test_low_value_item_green_channel():
    assert clearance_channel(10000, "electronics", True) == "green"
