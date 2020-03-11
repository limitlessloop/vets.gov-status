import unittest

from scripts.google_analytics.analytics_helpers import format_yearMonth


class FetchTransactionsTest(unittest.TestCase):
    def test_yearMonth_formatting(self):
        yearMonth = "201910"
        expected = "10/2019"
        actual = format_yearMonth(yearMonth)
        self.assertEqual(actual, expected)

    def test_yearMonth_formatting_removes_zero(self):
        yearMonth = "202001"
        expected = "1/2020"
        actual = format_yearMonth(yearMonth)
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
