import unittest
import pandas
import utilities.Utils as utils


class TestJsonToPandasDf(unittest.TestCase):
    def runTest(self):
        df = pandas.DataFrame([[1, 2, 3], [4, 5, 6]], columns=["a", "b", "c"])
        json = [["a", "b", "c"], [1, 2, 3], [4, 5, 6]]
        self.assertTrue(df.equals(utils.verticaljsontopandasdf(json)))


class TestSaveToDb(unittest.TestCase):
    def runTest(self):
        df = pandas.DataFrame([[1, 2, 3], [4, 5, 6]], columns=["a", "b", "c"])
        utils.savecsvtodb("a/a", df.to_csv())
