import unittest
import tools.eurostat as eurostat

class TestEurostat(unittest.TestCase):

    def test_download_economic_accounts_for_agri(self):
        eurostat.download_economic_agriculture_data()
        open('data/raw/economic-agriculture-data.tsv')

    def test_invalid_url_download_economic_accounts_for_agri(self):
        with self.assertRaises(SystemExit):
            eurostat.download_economic_agriculture_data('https://ec.europa.eu/eurostat/web/main/homsdfsde')

if __name__ == '__main__':
    unittest.main()