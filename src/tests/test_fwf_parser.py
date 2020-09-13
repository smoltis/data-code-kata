#!/usr/bin/env python3
'''
Unit tests for FWF parser
'''
import pytest
from file_parsers.fwf_parser import (parse_fwf_row,
                                     create_format_string)


@pytest.mark.parametrize("params, expected", [
    (('AAAAAAA', '2s 2s 3s', ['A', 'B', 'C']),
     {'A': 'AA', 'B': 'AA', 'C': 'AAA'}),
    (('AAAAAAA  ', '2s 2s 5s', ['A', 'B', 'C']),
     {'A': 'AA', 'B': 'AA', 'C': 'AAA  '})
])
def test_parse_fwf_row(params, expected):
    actual = parse_fwf_row(*params)
    assert actual == expected


def test_create_format_string():
    assert create_format_string(['1', '2', '4']) == '1s 2s 4s'
