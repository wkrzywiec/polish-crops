import unittest
import tools.imgw as imgw

class TestImgw(unittest.TestCase):

    def test_download_single_precipitation_report(self):
        years = [2019]
        reports = imgw.download_precipitation_reports(years)
        open('data/raw/o_m_2019.csv')
        self.assertDictEqual(reports, {2019: 'data/raw/o_m_2019.csv'})

    def test_download_four_precipitation_reports(self):
        years = [2016, 2017, 2018]
        expected_reports = {2016: 'data/raw/o_m_2016.csv', 2017: 'data/raw/o_m_2017.csv', 2018: 'data/raw/o_m_2018.csv' }
        reports = imgw.download_precipitation_reports(years)
        open('data/raw/o_m_2016.csv')
        open('data/raw/o_m_2017.csv')
        open('data/raw/o_m_2018.csv')
        self.assertDictEqual(reports, expected_reports)

    def test_incorrect_year_for_pecipitation_report_download(self):
        years = [1900]
        with self.assertRaises(SystemExit):
            imgw.download_precipitation_reports(years)


if __name__ == '__main__':
    unittest.main()