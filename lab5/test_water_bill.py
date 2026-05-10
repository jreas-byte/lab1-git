import unittest

from water_bill import calculate_bill, calculate_usage, create_summary


class TestWaterBill(unittest.TestCase):
    def test_calculate_usage(self):
        self.assertEqual(calculate_usage(100, 120), 20)
        self.assertEqual(calculate_usage(50, 50), 0)

    def test_calculate_usage_negative(self):
        with self.assertRaises(ValueError):
            calculate_usage(-1, 100)

    def test_calculate_usage_wrong_order(self):
        with self.assertRaises(ValueError):
            calculate_usage(120, 100)

    def test_calculate_bill(self):
        self.assertEqual(calculate_bill(10, 30), 300)
        self.assertEqual(calculate_bill(0, 30), 0)

    def test_calculate_bill_negative_usage(self):
        with self.assertRaises(ValueError):
            calculate_bill(-5, 30)

    def test_calculate_bill_negative_tariff(self):
        with self.assertRaises(ValueError):
            calculate_bill(10, -30)

    def test_create_summary(self):
        expected = {
            "usage": 20,
            "tariff": 30,
            "total": 600,
        }
        self.assertEqual(create_summary(100, 120, 30), expected)


if __name__ == "__main__":
    unittest.main()
