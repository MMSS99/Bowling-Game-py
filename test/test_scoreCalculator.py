import pytest
from src.scoreCalculator import ScoreCalculator

# cada 2 es un turno

@pytest.mark.state_n
def test_hitting_pins_regular():
    assert ScoreCalculator("12345123451234512345").calculateScore() == 60


@pytest.mark.state_n
def test_symbol_zero():
    assert ScoreCalculator("9-9-9-9-9-9-9-9-9-9-").calculateScore() == 90
    assert ScoreCalculator("9-3561368153258-7181").calculateScore() == 82


@pytest.mark.spare
def test_spare_not_extra():
    assert ScoreCalculator("9-3/613/815/-/8-7/8-").calculateScore() == 121


@pytest.mark.strike
def test_strike():
    # test strike
    assert ScoreCalculator("X9-9-9-9-9-9-9-9-9-").calculateScore() == 100
    assert ScoreCalculator("X9-X9-9-9-9-9-9-9-").calculateScore() == 110



@pytest.mark.strike
def test_two_strikes(): 
    # two strikes in a row is a double
    assert ScoreCalculator("XX9-9-9-9-9-9-9-9-").calculateScore() == 120


@pytest.mark.strike
def test_three_strikes():
    assert ScoreCalculator("XXX9-9-9-9-9-9-9-").calculateScore() == 141


@pytest.mark.extra_rolls
def test_one_pin_in_extra_roll():
    assert ScoreCalculator("9-3/613/815/-/8-7/8/8").calculateScore() == 131
    assert ScoreCalculator("5/5/5/5/5/5/5/5/5/5/5").calculateScore() == 150
    


@pytest.mark.extra_rolls
def test_two_strikes_in_extra_rolls():
    assert ScoreCalculator("9-9-9-9-9-9-9-9-9-XXX").calculateScore() == 111


@pytest.mark.extra_rolls
def test_one_strike_in_extra_roll():
    assert ScoreCalculator("8/549-XX5/53639/9/X").calculateScore() == 149


@pytest.mark.extra_rolls
def test_spare_in_extra_roll():
    assert ScoreCalculator("X5/X5/XX5/--5/X5/").calculateScore() == 175


@pytest.mark.extra_rolls
def test_triple_strike_before_extra_rolls():
    assert ScoreCalculator("XXXXXXXXXXXX").calculateScore() == 300


