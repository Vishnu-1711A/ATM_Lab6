# Lab 6 - Branch Coverage Testing
# SRN: PES2UG24CS264
import pytest
from atm_withdrawal import withdraw, pin_check, note_breakup


# ==========================================
# WITHDRAW FUNCTION - BRANCH COVERAGE
# ==========================================

def test_valid_savings_withdrawal():
    assert withdraw(5000, 1000, "savings", True) == 4000


def test_valid_current_withdrawal():
    assert withdraw(5000, 1000, "current", True) == 4000


def test_unknown_account():
    with pytest.raises(ValueError):
        withdraw(5000, 1000, "business", True)


def test_zero_amount():
    with pytest.raises(ValueError):
        withdraw(5000, 0, "savings", True)


def test_negative_amount():
    with pytest.raises(ValueError):
        withdraw(5000, -100, "savings", True)


def test_invalid_amount_not_multiple_of_100():
    with pytest.raises(ValueError):
        withdraw(5000, 150, "savings", True)


def test_withdrawal_within_daily_limit():
    assert withdraw(5000, 1000, "savings", True) == 4000


def test_savings_limit_exceeded():
    assert withdraw(60000, 25100, "savings", True) == "limit exceeded"


def test_current_limit_exceeded():
    assert withdraw(60000, 50100, "current", True) == "limit exceeded"


def test_own_bank_no_fee():
    assert withdraw(5000, 1000, "savings", True) == 4000


def test_other_bank_normal_fee():
    assert withdraw(5000, 1000, "savings", False) == 3980


def test_other_bank_high_fee():
    assert withdraw(20000, 11000, "current", False) == 8970


def test_insufficient_funds():
    assert withdraw(1000, 1000, "savings", False) == "insufficient funds"


def test_exact_balance_with_own_bank():
    assert withdraw(1000, 1000, "current", True) == 0


# ==========================================
# PIN CHECK - BRANCH COVERAGE
# ==========================================

def test_correct_pin():
    assert pin_check(1234, 1234, 0) == "ok"


def test_incorrect_pin_retry():
    assert pin_check(1111, 1234, 0) == "retry"


def test_wrong_pin_third_attempt():
    assert pin_check(1111, 1234, 2) == "card blocked"


def test_card_already_blocked():
    assert pin_check(1234, 1234, 3) == "card blocked"


def test_correct_pin_before_block_limit():
    assert pin_check(5678, 5678, 2) == "ok"


# ==========================================
# NOTE BREAKUP - BRANCH COVERAGE
# ==========================================

def test_note_breakup_exact_500():
    assert note_breakup(500) == (1, 0, 0)


def test_note_breakup_900():
    assert note_breakup(900) == (1, 2, 0)


def test_note_breakup_600():
    assert note_breakup(600) == (1, 0, 1)


def test_note_breakup_700():
    assert note_breakup(700) == (1, 1, 0)


def test_invalid_note_amount():
    with pytest.raises(ValueError):
        note_breakup(550)
