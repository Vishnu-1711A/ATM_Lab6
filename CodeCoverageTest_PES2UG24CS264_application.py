
import pytest
from atm_withdrawal import withdraw, pin_check, note_breakup


# ==========================================
# WITHDRAW FUNCTION TEST CASES
# ==========================================

def test_simple_withdrawal():
    assert withdraw(5000, 1000, "savings", True) == 4000


def test_unknown_account():
    with pytest.raises(ValueError):
        withdraw(5000, 1000, "business", True)


def test_zero_amount():
    with pytest.raises(ValueError):
        withdraw(5000, 0, "savings", True)


def test_negative_amount():
    with pytest.raises(ValueError):
        withdraw(5000, -100, "savings", True)


def test_invalid_amount():
    with pytest.raises(ValueError):
        withdraw(5000, 150, "savings", True)


def test_daily_limit_exceeded():
    assert withdraw(60000, 25100, "savings", True) == "limit exceeded"


def test_own_bank_withdrawal():
    assert withdraw(5000, 1000, "savings", True) == 4000


def test_other_bank_normal_fee():
    assert withdraw(5000, 1000, "savings", False) == 3980


def test_other_bank_high_fee():
    assert withdraw(20000, 11000, "current", False) == 8970


def test_insufficient_funds():
    assert withdraw(1000, 1000, "savings", False) == "insufficient funds"


def test_exact_balance():
    assert withdraw(1000, 1000, "current", True) == 0


# ==========================================
# PIN CHECK FUNCTION TEST CASES
# ==========================================

def test_correct_pin():
    assert pin_check(1234, 1234, 0) == "ok"


def test_wrong_pin():
    assert pin_check(1111, 1234, 0) == "retry"


def test_third_wrong_attempt():
    assert pin_check(1111, 1234, 2) == "card blocked"


def test_already_blocked():
    assert pin_check(1234, 1234, 3) == "card blocked"


# ==========================================
# NOTE BREAKUP FUNCTION TEST CASES
# ==========================================

def test_note_breakup_500_and_200():
    assert note_breakup(900) == (1, 2, 0)


def test_note_breakup_without_200():
    assert note_breakup(600) == (1, 0, 1)


def test_invalid_note_amount():
    with pytest.raises(ValueError):
        note_breakup(550)
