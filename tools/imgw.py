import tools.data_helper as helper

__base_url = 'https://dane.imgw.pl/data/dane_pomiarowo_obserwacyjne/dane_meteorologiczne/miesieczne/'
__precipitation_report_type = 'opad'
__precipitation_zip_name_pattern = '{}_m_o.zip'
__temperature_report_type = 'klimat'
__temperature_zip_name_pattern = '{}_m_k.zip'
__temperature_report_name_patter = 'k_m_t_{}.csv'
__raw_data_directory = 'data/raw/'

def download_precipitation_reports(years: list) -> dict:
    """Download precipitation reports from IMGW database

    Arguments:
        years {list} -- list of years for which to download reports

    Returns:
        dict -- dictionary of saved reports, where key = year, value = path_to_report
    """
    return __download_report_from_imgw(__precipitation_report_type, years)

def download_precipitation_report_dic() -> str:
    """Download description of columns in precipitation report

    Returns:
        str -- path to saved dictionary
    """
    content = helper.download_file('https://dane.imgw.pl/data/dane_pomiarowo_obserwacyjne/dane_meteorologiczne/miesieczne/opad/o_m_format.txt')
    return helper.save_file(content, __raw_data_directory + 'o_m_format.txt')

def download_temperature_reports(years: list) -> dict:
    """Download temperature reports from IMGW database

    Arguments:
        years {list} -- list of years for which to download reports

    Returns:
        dict -- dictionary of saved reports, where key = year, value = path_to_report
    """
    return __download_report_from_imgw(__temperature_report_type, years)

def download_temperature_report_dic() -> str:
    """Download description of columns in temperature report

    Returns:
        str -- path to saved dictionary
    """
    content = helper.download_file('https://dane.imgw.pl/data/dane_pomiarowo_obserwacyjne/dane_meteorologiczne/miesieczne/klimat/k_m_t_format.txt')
    return helper.save_file(content, __raw_data_directory + 'k_m_t_format.txt')

def __download_report_from_imgw(report_type: str, years: list) -> dict:
    reports = {}
    zip_name_pattern = __indicate_file_name_pattern(report_type)

    for year in years:
        content = __download_zipped_file(report_type, year, zip_name_pattern)
        zipped_file_path = helper.save_file(content, __raw_data_directory + zip_name_pattern.format(str(year)))
        unzipped_file_path = __extract_report_from_zip(zipped_file_path, report_type, year)
        reports[year] = unzipped_file_path
        helper.delete_file(zipped_file_path)
    return reports

def __indicate_file_name_pattern(report_type):
    if report_type == __precipitation_report_type:
        return __precipitation_zip_name_pattern
    elif report_type == __temperature_report_type:
        return __temperature_zip_name_pattern
    else:
        raise SystemExit("file_name_pattern to be extracted from zip can't be indicated. Reason: there is no report with a type: " + report_type)

def __extract_report_from_zip(zipped_file_path: str, report_type: str, year: int):
    if report_type == __precipitation_report_type:
        return helper.unzip_zip_file(zipped_file_path)
    elif report_type == __temperature_report_type:
        return helper.unzip_zip_file(zipped_file_path, __temperature_report_name_patter.format(str(year)))
    else:
        raise SystemExit("Can't extract report from zip. Reason: there is no report with a type: " + report_type)

def __download_zipped_file(type: str, year: int, zip_name_pattern: str):
    return helper.download_file(__base_url + type + '/' + str(year) + '/' + zip_name_pattern.format(str(year)))