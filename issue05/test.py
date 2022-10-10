import what_is_year_now
import pytest
from unittest.mock import MagicMock, patch


@patch('urllib.request.urlopen')
def test_format_one(urlopen):
    mock = MagicMock()
    mock.read.return_value = '{"$id":"1",' \
                             '"currentDateTime":"2022-10-10T11:21Z",' \
                             '"utcOffset":"00:00:00",' \
                             '"isDayLightSavingsTime":false,' \
                             '"dayOfTheWeek":"Monday",' \
                             '"timeZoneName":"UTC",' \
                             '"currentFileTime":133098749833987610,' \
                             '"ordinalDate":"2022-283",' \
                             '"serviceResponse":null}'
    mock.__enter__.return_value = mock
    urlopen.return_value = mock
    assert what_is_year_now.what_is_year_now() == 2022


@patch('urllib.request.urlopen')
def test_format_two(urlopen):
    mock = MagicMock()
    mock.read.return_value = '{"$id":"1",' \
                             '"currentDateTime":"10.10.2022T11:21Z",' \
                             '"utcOffset":"00:00:00",' \
                             '"isDayLightSavingsTime":false,' \
                             '"dayOfTheWeek":"Monday",' \
                             '"timeZoneName":"UTC",' \
                             '"currentFileTime":133098749833987610,' \
                             '"ordinalDate":"2022-283",' \
                             '"serviceResponse":null}'
    mock.__enter__.return_value = mock
    urlopen.return_value = mock
    assert what_is_year_now.what_is_year_now() == 2022


@patch('urllib.request.urlopen')
def test_exception(urlopen):
    mock = MagicMock()
    mock.read.return_value = '{"$id":"1",' \
                             '"currentDateTime":"10102022T11:21Z",' \
                             '"utcOffset":"00:00:00",' \
                             '"isDayLightSavingsTime":false,' \
                             '"dayOfTheWeek":"Monday",' \
                             '"timeZoneName":"UTC",' \
                             '"currentFileTime":133098749833987610,' \
                             '"ordinalDate":"2022-283",' \
                             '"serviceResponse":null}'
    mock.__enter__.return_value = mock
    urlopen.return_value = mock
    with pytest.raises(ValueError):
        what_is_year_now.what_is_year_now()