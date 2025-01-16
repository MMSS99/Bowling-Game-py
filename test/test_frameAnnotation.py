import pytest
from src.scoreCalculator import ScoreCalculator

def test_frameAnnotation():
    testingclass = ScoreCalculator('12345123451234512345')
    assert testingclass._ScoreCalculator__frameAnnotation() == [['1', '2'], ['3', '4'], ['5', '1'], ['2', '3'], ['4', '5'], ['1', '2'], ['3', '4'], ['5', '1'], ['2', '3'], ['4', '5']]
    testingclass = ScoreCalculator('8/549-XX5/53639/9/X')
    assert testingclass._ScoreCalculator__frameAnnotation() == [['8', '/'], ['5', '4'], ['9', '-'], ['X'], ['X'], ['5', '/'], ['5', '3'], ['6', '3'], ['9', '/'], ['9', '/', 'X']]

