#!/usr/bin/env python3

from file_parsers.fwf_generator import generate_fixed_width_file


if __name__ == '__main__':
    import argparse
    import os
    DEFAULT_SPEC_FILENAME = 'spec.json'
    DEFAULT_N_ROWS = 100
    DEFAULT_FWF_FILENAME = 'fixed.txt'

    parser = argparse.ArgumentParser(
        description='''Generate fixed width file (FWF)
                       of random characters based on spec (JSON)''',
        epilog='''Characters for the values
                are random lower and upper alphanumeric''')
    parser.add_argument('-s', '--spec', type=str,
                        default=os.environ.get('SPEC_FILENAME',
                                               DEFAULT_SPEC_FILENAME),
                        help='Specification JSON file. [{}]'
                        .format(DEFAULT_SPEC_FILENAME))
    parser.add_argument('-o', '--out', type=str,
                        default=os.environ.get('FWF_FILENAME',
                                               DEFAULT_FWF_FILENAME),
                        help='Output fixed width file name. [{}]'
                        .format(DEFAULT_FWF_FILENAME))
    parser.add_argument('-n', '--n_rows', type=int,
                        default=os.environ.get('N_ROWS',
                                               DEFAULT_N_ROWS),
                        help='Nuber of data rows in the output file. [{}]'
                        .format(DEFAULT_N_ROWS))
    parser.add_argument('-r', '--rand', dest='rand',
                        action='store_true',
                        help='Randomize data. [False]')
    parser.set_defaults(rand=False)
    args = parser.parse_args()
    generate_fixed_width_file(args.out, args.spec, args.n_rows, args.rand)
