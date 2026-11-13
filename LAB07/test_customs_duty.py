
import pytest
from hypothesis import given, strategies as st

from customs_duty import parse_declaration, duty_amount, hs_chapter


# Fuzz testing: parse_declaration
@given(st.text() | st.none())
def test_parse_declaration_no_crash(s):
    try:
        parse_declaration(s)
    except ValueError:
        pass


# Fuzz testing: duty_amount
@given(st.text() | st.none())
def test_duty_amount_no_crash(s):
    try:
        duty_amount(s)
    except ValueError:
        pass


# Fuzz testing: hs_chapter
@given(st.text() | st.none())
def test_hs_chapter_no_crash(s):
    try:
        hs_chapter(s)
    except ValueError:
        pass


# Valid input tests
def test_parse_declaration_valid():
    assert parse_declaration(" Electronics:25000 ") == ("electronics", 25000.0)


def test_duty_amount_valid():
    assert duty_amount("25000@20") == 5000


def test_hs_chapter_valid():
    assert hs_chapter("8517.12") == 85


# Invalid input tests
@pytest.mark.parametrize("value", [None, "", "hello", "abc:xyz", ":25000"])
def test_invalid_declaration(value):
    with pytest.raises(ValueError):
        parse_declaration(value)


@pytest.mark.parametrize("value", [None, "", "hello", "25000@abc"])
def test_invalid_duty(value):
    with pytest.raises(ValueError):
        duty_amount(value)


@pytest.mark.parametrize("value", [None, "", "abc.xyz", "8", "8517.A"])
def test_invalid_hs_code(value):
    with pytest.raises(ValueError):
        hs_chapter(value)
