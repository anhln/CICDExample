"""
Unit test for calculator
"""

import calculator


class TestCalculator:

    def test_addition(self):
        assert 4 == calculator.add(2, 2)

    def test_subtraction(self):
        assert 4 == calculator.subtract(6, 2)
        



