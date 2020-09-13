#!/usr/bin/env python3
'''
Unit tests for spec reader
'''
import os
import pytest
from file_parsers.specification import (read_spec, create_spec,
                                        parse_spec, sanity_check)


def test_read_spec_from_file():
    pwd = os.path.dirname(os.path.realpath(__file__))
    actual = read_spec(os.path.join(pwd, 'spec_test.json'))
    assert type(actual) == dict
    assert len(actual) > 0
    assert 'ColumnNames' in actual


@pytest.mark.parametrize("spec", [{'ColumnNames': ['c1']},
                                  {'ColumnNames': ['c1'], 'Offsets': ['1']}])
def test_sanity_check_attr_error(spec):
    with pytest.raises(AttributeError):
        sanity_check(spec)


@pytest.mark.parametrize("spec", [{'ColumnNames': ['c1'],
                                   'Offsets': '2',
                                   'FixedWidthEncoding': 'utf-8',
                                   'IncludeHeader': 'True',
                                   'DelimitedEncoding': 'utf-8'},
                                  {'ColumnNames': 'c1',
                                   'Offsets': ['2'],
                                   'FixedWidthEncoding': 'utf-8',
                                   'IncludeHeader': 'True',
                                   'DelimitedEncoding': 'utf-8'}])
def test_sanity_check_type_error(spec):
    spec = create_spec(spec)
    with pytest.raises(TypeError):
        sanity_check(spec)


@pytest.mark.parametrize("spec", [{'ColumnNames': ['c1'],
                                   'Offsets': ['2'],
                                   'FixedWidthEncoding': 'utf-8',
                                   'IncludeHeader': 'true',
                                   'DelimitedEncoding': 'utf-8'},
                                  {'ColumnNames': ['c1', 'c2'],
                                   'Offsets': ['2'],
                                   'FixedWidthEncoding': 'utf-8',
                                   'IncludeHeader': 'True',
                                   'DelimitedEncoding': 'utf-8'},
                                  {'ColumnNames': ['c1'],
                                   'Offsets': ['0'],
                                   'FixedWidthEncoding': 'utf-8',
                                   'IncludeHeader': 'True',
                                   'DelimitedEncoding': 'utf-8'},
                                  {'ColumnNames': ['c1'],
                                   'Offsets': ['1'],
                                  'FixedWidthEncoding': 'utf-8',
                                   'IncludeHeader': 'True',
                                   'DelimitedEncoding': 'utf-8'},
                                  {'ColumnNames': ['c1'],
                                   'Offsets': ['X'],
                                   'FixedWidthEncoding': 'utf-8',
                                   'IncludeHeader': 'True',
                                   'DelimitedEncoding': 'utf-8'}])
def test_sanity_check_value_error(spec):
    spec = create_spec(spec)
    with pytest.raises(ValueError):
        sanity_check(spec)


@pytest.mark.parametrize("spec", [{'ColumnNames': ['c1'],
                                   'Offsets': ['2'],
                                   'FixedWidthEncoding': 'utf-8',
                                   'IncludeHeader': 'True',
                                   'DelimitedEncoding': 'winpy-8'}])
def test_sanity_check_lookup_error(spec):
    spec = create_spec(spec)
    with pytest.raises(LookupError):
        sanity_check(spec)


@pytest.mark.parametrize("spec", [{'ColumnNames': ['c1'],
                                   'Offsets': ['2'],
                                   'FixedWidthEncoding': 'utf-8',
                                   'IncludeHeader': 'True',
                                   'DelimitedEncoding': 'windows-1251'},
                                  {'ColumnNames': ['c1', 'c2'],
                                   'Offsets': ['2', '5'],
                                   'FixedWidthEncoding': 'utf-8',
                                   'IncludeHeader': 'True',
                                   'DelimitedEncoding': 'windows-1251'}])
def test_create_spec_as_namedtuple(spec):
    actual = create_spec(spec)
    assert actual.ColumnNames[0] == 'c1'
    assert actual.IncludeHeader == 'True'
    assert actual.DelimitedEncoding == 'windows-1251'
    assert actual.Offsets[0] == '2'


def test_parse_spec():
    pwd = os.path.dirname(os.path.realpath(__file__))
    actual = parse_spec(os.path.join(pwd, 'spec_test.json'))
    assert actual.DelimitedEncoding == 'utf-8'
