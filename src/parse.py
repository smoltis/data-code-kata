#!/usr/bin/env python3

from file_parsers.fwf_parser import convert_file


if __name__ == '__main__':
    import argparse
    import os
    DEFAULT_SPEC_FILENAME = 'spec.json'
    DEFAULT_FWF_FILENAME = 'fixed.txt'
    DEFAULT_CSV_FILENAME = 'delimited.csv'

    parser = argparse.ArgumentParser(
        description='''Parse fixed width file (FWF)
                       and produce comma separated (CSV)
                       as per format specification (JSON)''')
    parser.add_argument('-s', '--spec', type=str,
                        default=os.environ.get('SPEC_FILENAME',
                                               DEFAULT_SPEC_FILENAME),
                        help='Specification JSON file. [{}]'
                        .format(DEFAULT_SPEC_FILENAME))
    parser.add_argument('-i', '--input', type=str,
                        default=os.environ.get('FWF_FILENAME',
                                               DEFAULT_FWF_FILENAME),
                        help='Input FWF file name. [{}]'
                        .format(DEFAULT_FWF_FILENAME))
    parser.add_argument('-o', '--output', type=str,
                        default=os.environ.get('CSV_FILENAME',
                                               DEFAULT_CSV_FILENAME),
                        help='Output CSV file name. [{}]'
                        .format(DEFAULT_CSV_FILENAME))
    args = parser.parse_args()
    convert_file(args.input, args.output, args.spec)
