import pytest


@pytest.mark.state_n
def test_hitting_pins_regular():

    pins = "12345123451234512345"
    total = 60


@pytest.mark.state_n
def test_symbol_zero():
    # test symbol -

    pins = "9-9-9-9-9-9-9-9-9-9-"
    total = 90

    pins = "9-3561368153258-7181"
    total = 82


@pytest.mark.spare
def test_spare_not_extra():

    pins = "9-3/613/815/-/8-7/8-"
    total = 121


@pytest.mark.strike
def test_strike():
    # test strike

    pins = "X9-9-9-9-9-9-9-9-9-"
    total = 100



    pins = "X9-X9-9-9-9-9-9-9-"
    total = 110


@pytest.mark.strike
def test_two_strikes(): 
    # two strikes in a row is a double

    pins = "XX9-9-9-9-9-9-9-9-"
    total = 120


@pytest.mark.strike
def test_three_strikes():

    pins = "XXX9-9-9-9-9-9-9-"
    total = 141


@pytest.mark.extra_rolls
def test_one_pin_in_extra_roll():

    pins = "9-3/613/815/-/8-7/8/8"
    total = 131



    pins = "5/5/5/5/5/5/5/5/5/5/5"
    total = 150


@pytest.mark.extra_rolls
def test_two_strikes_in_extra_rolls():
    # two strikes in extra rolls

    pins = "9-9-9-9-9-9-9-9-9-XXX"
    total = 111


@pytest.mark.extra_rolls
def test_one_strike_in_extra_roll():

    pins = "8/549-XX5/53639/9/X"
    total = 149


@pytest.mark.extra_rolls
def test_spare_in_extra_roll():

    pins = "X5/X5/XX5/--5/X5/"
    total = 175


@pytest.mark.extra_rolls
def test_triple_strike_before_extra_rolls():

    pins = "XXXXXXXXXXXX"
    total = 300

