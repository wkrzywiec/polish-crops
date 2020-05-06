import unittest
import tools.eurostat as eurostat

class TestEurostat(unittest.TestCase):

    def test_download_economic_accounts_for_agri(self):
        eurostat.download_crop_prices()
        open('data/raw/crop-prices.tsv')

    def test_invalid_url_download_economic_accounts_for_agri(self):
        with self.assertRaises(SystemExit):
            eurostat.download_crop_prices('https://ec.europa.eu/eurostat/web/main/homsdfsde')

if __name__ == '__main__':
    unittest.main()