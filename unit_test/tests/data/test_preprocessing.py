import pytest
from unit_test.data.preprocessing import row_to_list, convert_to_int


def test_for_clean_row():
    assert row_to_list('2,081\t314,942\n') == ['2,081', '314,942']


def test_for_missing_area():
    actual = row_to_list('\t293,410\n')
    expected = None
    message = ('row_to_list("\t293,410\n") returned'
               '{0} instead of {1}'.format(actual, expected))
    assert actual is expected, message


def test_for_missing_tab():
    assert row_to_list('1,41234,323\n') is None


def test_on_string_with_one_comma():
    value = convert_to_int('2,081')
    assert isinstance(value, int), f'The value {value} has to be int'

