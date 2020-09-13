import json
import codecs
from collections import namedtuple


def read_spec(filename):
    with open(filename, 'r') as json_file:
        data = json.load(json_file)
        return data


def create_spec(data):
    Specification = namedtuple('Specification', sorted(data))
    return Specification(**data)


def sanity_check(spec):
    attributes = ['ColumnNames', 'Offsets',
                  'IncludeHeader', 'FixedWidthEncoding',
                  'DelimitedEncoding']
    print('Specification Sanity Check:', end='')
    for attr in attributes:
        try:
            getattr(spec, attr)
        except AttributeError:
            print("Attribute {}...not found".format(attr))
    if not isinstance(spec.ColumnNames, list):
        raise TypeError('ColumnNames must be a JSON array')
    if not isinstance(spec.Offsets, list):
        raise TypeError('Offsets must be be a JSON array')
    if len(spec.ColumnNames) > len(spec.Offsets):
        raise ValueError('All columns must have offsets')
    if len(spec.ColumnNames) < len(spec.Offsets):
        raise ValueError('Too many Offsets')
    for num in spec.Offsets:
        int(num)    # raises ValueError
    for clen, olen in zip(map(len, spec.ColumnNames), spec.Offsets):
        if clen > int(olen):
            raise ValueError('Column name is longer than column width')
    codecs.lookup(spec.FixedWidthEncoding)
    codecs.lookup(spec.DelimitedEncoding)
    if spec.IncludeHeader not in ('True', 'False'):
        raise ValueError('IncludeHeader must be True or False')
    print('OK')


def parse_spec(filename):
    spec = create_spec(read_spec(filename))
    sanity_check(spec)
    return spec
