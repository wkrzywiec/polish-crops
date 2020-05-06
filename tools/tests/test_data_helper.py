import unittest
import tools.data_helper as helper

class TestDataHelper(unittest.TestCase):

    def test_invalid_url_download_economic_accounts_for_agri(self):
        with self.assertRaises(SystemExit):
            helper.download_file('https://ec.europa.eu/eurostat/web/main/homsdfsde')

if __name__ == '__main__':
    unittest.main()