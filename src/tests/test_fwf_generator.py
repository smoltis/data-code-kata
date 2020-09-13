#!/usr/bin/env python3
'''
Unit tests for FWF generator
'''
import pytest
import io
from file_parsers.fwf_generator import random_string, write_header, write_rows


@pytest.mark.parametrize("params, expected", [
    (('AAAAAAA', 2), 'AA'),
    (("B", None), 'B'),
    (("BB", 2), 'BB'),
])
def test_random_string(params, expected):
    str_obj, length = params
    actual = random_string(str_obj, length)
    assert actual == expected


@pytest.mark.parametrize("params, expected", [
    ((['1', '2', '3'], ['A', 'B', 'C']), 'AB C  \n'),
    ((['1'], ['B']), 'B\n'),
    ((['2'], ['BB']), 'BB\n'),
])
def test_write_header(params, expected):
    offsets, columns = params
    string_out = io.StringIO()
    write_header(offsets, columns, string_out)
    assert string_out.getvalue() == expected


@pytest.mark.parametrize("params, expected", [
    ((['1', '2', '3'], 1, None), 'AABABC'),
    ((['1', '2', '2'], 3, None), 'AABAB')
])
def test_write_rows_ltters_data(params, expected):
    offsets, N_rows, rand = params
    string_out = io.StringIO()
    write_rows(offsets, N_rows, rand, string_out)
    actual = string_out.getvalue().split('\n')
    for line in actual:
        assert line == expected
    assert len(actual) == N_rows


@pytest.mark.parametrize("params", [
    (['1', '2', '3'], 1, True),
    (['1', '2', '2'], 3, True)
])
def test_write_rows_random_data(params):
    offsets, N_rows, rand = params
    string_out = io.StringIO()
    write_rows(offsets, N_rows, rand, string_out)
    actual = string_out.getvalue().split('\n')
    value_length = sum(map(int, offsets))
    assert len(actual) == N_rows
    for line in actual:
        assert len(line) == value_length
        assert line.isalnum() is True
