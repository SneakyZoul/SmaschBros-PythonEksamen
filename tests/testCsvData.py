import unittest
import os
import pandas as pd
from config.definitions import ROOT_DIR


class TestCsvData(unittest.TestCase):
    def test_steve_csv_data(self):
        data = pd.read_csv(os.path.join(ROOT_DIR, 'src', 'scraping', 'data.csv'))
        steve = (data[data['character'] == 'Steve'][['firstPlaces', 'secondPlaces']])
        steve_first_place = steve['firstPlaces'].item()
        steve_second_place = steve['secondPlaces'].item()
        actual = [steve_first_place, steve_second_place]
        expected = [8, 3]
        self.assertEqual(expected, actual)

    def test_byleth_csv_data(self):
        data = pd.read_csv(os.path.join(ROOT_DIR, 'src', 'scraping', 'data.csv'))
        byleth = (data[data['character'] == 'Byleth'][['firstPlaces', 'secondPlaces']])
        byleth_first_place = byleth['firstPlaces'].item()
        byleth_second_place = byleth['secondPlaces'].item()
        actual = [byleth_first_place, byleth_second_place]
        expected = [12, 4]
        self.assertEqual(expected, actual)

    def test_wario_csv_data(self):
        data = pd.read_csv(os.path.join(ROOT_DIR, 'src', 'scraping', 'data.csv'))
        wario = (data[data['character'] == 'Wario'][['firstPlaces', 'secondPlaces']])
        wario_first_place = wario['firstPlaces'].item()
        wario_second_place = wario['secondPlaces'].item()
        actual = [wario_first_place, wario_second_place]
        expected = [17, 16]
        self.assertEqual(expected, actual)

    def test_shiek_csv_data(self):
        data = pd.read_csv(os.path.join(ROOT_DIR, 'src', 'scraping', 'data.csv'))
        shiek = (data[data['character'] == 'Sheik'][['firstPlaces', 'secondPlaces']])
        shiek_first_place = shiek['firstPlaces'].item()
        shiek_second_place = shiek['secondPlaces'].item()
        actual = [shiek_first_place, shiek_second_place]
        expected = [2, 3]
        self.assertEqual(expected, actual)

    def test_falco_csv_data(self):
        data = pd.read_csv(os.path.join(ROOT_DIR, 'src', 'scraping', 'data.csv'))
        falco = (data[data['character'] == 'Falco'][['firstPlaces', 'secondPlaces']])
        falco_first_place = falco['firstPlaces'].item()
        falco_second_place = falco['secondPlaces'].item()
        actual = [falco_first_place, falco_second_place]
        expected = [0, 1]
        self.assertEqual(expected, actual)

    def test_fox_csv_data(self):
        data = pd.read_csv(os.path.join(ROOT_DIR, 'src', 'scraping', 'data.csv'))
        fox = (data[data['character'] == 'Fox'][['firstPlaces', 'secondPlaces']])
        fox_first_place = fox['firstPlaces'].item()
        fox_second_place = fox['secondPlaces'].item()
        actual = [fox_first_place, fox_second_place]
        expected = [3, 10]
        self.assertEqual(expected, actual)

    def test_wolf_csv_data(self):
        data = pd.read_csv(os.path.join(ROOT_DIR, 'src', 'scraping', 'data.csv'))
        wolf = (data[data['character'] == 'Wolf'][['firstPlaces', 'secondPlaces']])
        wolf_first_place = wolf['firstPlaces'].item()
        wolf_second_place = wolf['secondPlaces'].item()
        actual = [wolf_first_place, wolf_second_place]
        expected = [9, 7]
        self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main()
