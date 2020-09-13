'''
FWF to CSV parser
'''
import csv
from struct import Struct
from .specification import parse_spec


def parse_fwf_row(line, fmtstring, columns):
    fieldstruct = Struct(fmtstring)
    unpacked_unicode = fieldstruct.unpack_from(line.encode())
    values = (c.decode() for c in unpacked_unicode)
    return dict(zip(columns, values))


def create_format_string(offsets):
    return ' '.join(map(lambda c: c + 's', offsets))


def convert_file(fwf_filename, csv_filename, spec_filename):
    spec = parse_spec(spec_filename)
    fmtstring = create_format_string(spec.Offsets)
    columns = spec.ColumnNames
    with open(fwf_filename, 'r',
              encoding=spec.FixedWidthEncoding) as fwf_file:
        with open(csv_filename, 'w', newline='',
                  encoding=spec.DelimitedEncoding) as csv_file:
            csv_writer = csv.DictWriter(csv_file, fieldnames=columns)
            if spec.IncludeHeader == 'True':
                csv_writer.writeheader()
                fwf_file.readline()
            for line in fwf_file:
                row = parse_fwf_row(line, fmtstring, columns)
                csv_writer.writerow(row)
