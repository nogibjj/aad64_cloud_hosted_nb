import unittest
import pandas as pd


class TestDF(unittest.TestCase):
    def test_df_shape(self):
        df = pd.read_csv("your_file.csv")  # replace with your file path
        self.assertEqual(df.shape, (32561, 15))


if __name__ == "__main__":
    unittest.main()
