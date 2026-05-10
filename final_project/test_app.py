import unittest

from app import analyze_log


class TestAnalyzeLog(unittest.TestCase):
    def test_log_with_error(self):
        self.assertEqual(
            analyze_log("ERROR Database connection failed"),
            "Знайдено помилку ERROR",
        )

    def test_log_without_error(self):
        self.assertEqual(
            analyze_log("INFO Application started"),
            "Помилок не знайдено",
        )

    def test_empty_log(self):
        with self.assertRaises(ValueError):
            analyze_log("")

    def test_spaces_log(self):
        with self.assertRaises(ValueError):
            analyze_log("   ")

    def test_not_string(self):
        with self.assertRaises(ValueError):
            analyze_log(123)


if __name__ == "__main__":
    unittest.main()
