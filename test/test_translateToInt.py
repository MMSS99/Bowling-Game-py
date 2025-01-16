import pytest
from src.scoreCalculator import ScoreCalculator

def test_translateToInt():
    testingclass = ScoreCalculator('12345123451234512345')
    assert testingclass._ScoreCalculator__translateToInt() == [3, 7, 6, 5, 9, 3, 7, 6, 5, 9]
    testingclass = ScoreCalculator('8/549-XX5/53639/9/X')
    assert testingclass._ScoreCalculator__translateToInt() == [15, 9, 9, 25, 20, 15, 8, 9, 19, 20]