'''
FWF file generator
'''
import random
from .specification import parse_spec
from string import ascii_uppercase, ascii_letters, digits


def write_header(offsets, columns, file):
    for width, col_name in zip(offsets, columns):
        print('{0:{width}}'.format(col_name, width=width),
              end='',
              file=file)
    file.write('\n')


def write_rows(offsets, N_rows, rand, file):
    for i in range(0, N_rows):
        for width in map(int, offsets):
            data = ascii_uppercase
            value = data[:width]
            if rand:
                abc = digits+ascii_letters+digits
                data = ''.join(random.sample(abc, len(abc)))
                value = random_string(data, width)
            print('{0:{width}}'.format(value, width=width),
                  end='',
                  file=file)
        if i < N_rows-1:
            file.write('\n')


def random_string(str_obj, length=None):
    shuffled = random.sample(str_obj,
                             len(str_obj))
    if not length:
        return ''.join(shuffled)

    sampled = random.sample(shuffled, length)
    return ''.join(sampled)


def generate_fixed_width_file(csv_filename, spec, N_rows, rand=False):
    spec = parse_spec(spec)
    with open(csv_filename, 'w', encoding=spec.FixedWidthEncoding) as csv_file:
        if spec.IncludeHeader == 'True':
            write_header(spec.Offsets, spec.ColumnNames, csv_file)
        write_rows(spec.Offsets, N_rows, rand, csv_file)
