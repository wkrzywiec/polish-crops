import unittest
import tools.eurostat as eurostat

class TestEurostat(unittest.TestCase):

    def test_download_economic_accounts_for_agri(self):
        eurostat.download_crop_prices()
        open('data/raw/apri_ap_crpouta.tsv')

    def test_download_crop_categories_dic(self):
        eurostat.download_crop_categories_dic()
        open('data/raw/prod_veg.dic')

if __name__ == '__main__':
    unittest.main()