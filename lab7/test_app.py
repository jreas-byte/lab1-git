import unittest

from app import calculate_payroll


class TestCalculatePayroll(unittest.TestCase):
    def test_basic_case(self):
        employees = [
            {"name": "Іван", "hours": 40, "rate": 100},
            {"name": "Марія", "hours": 30, "rate": 150},
        ]
        expected = [
            {"name": "Іван", "salary": 4000},
            {"name": "Марія", "salary": 4500},
        ]
        self.assertEqual(calculate_payroll(employees), expected)

    def test_empty_list(self):
        self.assertEqual(calculate_payroll([]), [])

    def test_zero_hours(self):
        employees = [{"name": "Олег", "hours": 0, "rate": 100}]
        expected = [{"name": "Олег", "salary": 0}]
        self.assertEqual(calculate_payroll(employees), expected)

    def test_zero_rate(self):
        employees = [{"name": "Анна", "hours": 10, "rate": 0}]
        expected = [{"name": "Анна", "salary": 0}]
        self.assertEqual(calculate_payroll(employees), expected)

    def test_negative_hours(self):
        employees = [{"name": "Петро", "hours": -1, "rate": 100}]
        with self.assertRaises(ValueError):
            calculate_payroll(employees)

    def test_negative_rate(self):
        employees = [{"name": "Олена", "hours": 10, "rate": -50}]
        with self.assertRaises(ValueError):
            calculate_payroll(employees)


if __name__ == "__main__":
    unittest.main()
