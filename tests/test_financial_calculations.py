from tests import unittest
import package.calculations as calc

class TestFutureValueCalculator(unittest.TestCase):
    def test_positive_interest_rate(self):
        result = calc.FutureValueCalculator(1000, 0.05, 2)
        self.assertEqual(result.balance, 1102.5)

    def test_zero_principal(self):
        with self.assertRaises(ValueError):
            result = calc.FutureValueCalculator(0, 0.05, 1000)

    def test_negative_interest_rate(self):
        with self.assertRaises(ValueError):
            result = calc.FutureValueCalculator(1000, -0.05, 2)

    def test_negative_time(self):
        with self.assertRaises(ValueError):
            result = calc.FutureValueCalculator(1000, 0.05, -2)

    def test_non_numeric_inputs(self):
        result = calc.FutureValueCalculator("1000", "0.05", "2")

    def test_invalid_rate_string(self):
        with self.assertRaises(ValueError):
            result = calc.FutureValueCalculator(1000, "invalid_rate", 2)

    def test_invalid_time_string(self):
        with self.assertRaises(ValueError):
            result = calc.FutureValueCalculator(1000, 0.05, "invalid_time")

    def test_calculate_values_over_time(self):
        calculator = calc.FutureValueCalculator(1000, 0.05, 2)
        values_over_time = calculator.calculate_values_over_time()
        expected_values = [(1, 1050.0), (2, 1102.5)]
        self.assertEqual(values_over_time, expected_values)

    def test_plot(self):
        calculator = calc.FutureValueCalculator(1000, 0.05, 2)
        calculator.plot()  # Check if the plot function runs without errors

class TestPresentValueCalculator(unittest.TestCase):
    def test_positive_inputs(self):
        calculator = calc.PresentValueCalculator(1102.5, 0.05, 2)
        self.assertEqual(calculator.present_value, 1000.0)

    def test_zero_future_value(self):
        with self.assertRaises(ValueError):
            result = calc.PresentValueCalculator(0, 0.05, 1000)

    def test_calculate_values_over_time(self):
        calculator = calc.PresentValueCalculator(1102.5, 0.05, 2)
        values_over_time = calculator.calculate_values_over_time()
        expected_values = [(2, 1050.0), (1, 1000.0)]
        self.assertEqual(values_over_time, expected_values)

    def test_plot(self):
        calculator = calc.PresentValueCalculator(1102.5, 0.05, 2)
        calculator.plot()

    def test_non_numeric_inputs(self):
        result = calc.PresentValueCalculator("1102.5", "0.05", "2")

    def test_invalid_rate_string(self):
        with self.assertRaises(ValueError):
            result = calc.PresentValueCalculator(1102.5, "invalid_rate", 2)

    def test_invalid_time_string(self):
        with self.assertRaises(ValueError):
            result = calc.PresentValueCalculator(1102.5, 0.05, "invalid_time")

class TestCAGR(unittest.TestCase):
    def test_positive_inputs(self):
        calculator = calc.CAGR(1000, 2000, 5)
        self.assertAlmostEqual(calculator.rate * 100, 14.87, places=2)

    def test_zero_principal(self):
        with self.assertRaises(ValueError):
            result = calc.CAGR(0, 2000, 5)

    def test_zero_future_value(self):
        with self.assertRaises(ValueError):
            result = calc.CAGR(1000, 0, 5)

    def test_zero_time(self):
        with self.assertRaises(ValueError):
            result = calc.CAGR(1000, 2000, 0)

    def test_negative_principal(self):
        with self.assertRaises(ValueError):
            result = calc.CAGR(-1000, 2000, 5)

    def test_negative_future_value(self):
        with self.assertRaises(ValueError):
            result = calc.CAGR(1000, -2000, 5)

    def test_negative_time(self):
        with self.assertRaises(ValueError):
            result = calc.CAGR(1000, 2000, -5)

    def test_non_numeric_inputs(self):
        result = calc.CAGR("1000", "2000", "5")

    def test_invalid_principal_string(self):
        with self.assertRaises(ValueError):
            result = calc.CAGR("invalid_principal", 2000, 5)

    def test_invalid_future_value_string(self):
        with self.assertRaises(ValueError):
            result = calc.CAGR(1000, "invalid_future_value", 5)

    def test_invalid_time_string(self):
        with self.assertRaises(ValueError):
            result = calc.CAGR(1000, 2000, "invalid_time")

if __name__ == '__main__':
    unittest.main()
