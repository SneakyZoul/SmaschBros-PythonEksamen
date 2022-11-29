import unittest
import pandas as pd
from src.handlingdata import GettingData


class TestGettingData(unittest.TestCase):
    def test_fetching_data(self):
        actual = GettingData.fetching_data()
        expected = pd.DataFrame()
        self.assertEqual(type(actual), type(expected))  # add assertion here


if __name__ == '__main__':
    unittest.main()
