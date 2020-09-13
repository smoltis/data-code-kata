import csv
import random
from sys import getsizeof
from datetime import timedelta
from datetime import datetime

random.seed(42)

NAMES_SET = []
SURNAMES_SET = []


def random_date(start, end):
    """
    This function will return a random datetime between
    two datetime objects.
    """
    delta = end - start
    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
    random_second = random.randrange(int_delta)
    return start + timedelta(seconds=random_second)


def get_name():
    return random.choice(NAMES_SET)


def get_surname():
    return random.choice(SURNAMES_SET)


def get_post_code():
    return random.randint(1000, 9999)


def get_addr():
    h = random.randrange(999)
    p = random.choice(['St.', 'Ln.', 'Dr.', 'Ave.', 'Rd.'])
    s = random.choice(['VIC', 'NSW', 'ACT', 'NT', 'WA', 'SA', 'TAS', 'QLD'])
    u = random.choice(['', 'U'+str(random.randrange(99))+', '])
    n = random.choice([get_name(), get_surname()])
    addr = '{} {} {} {} {} {}'.format(u, h, n, p, s, get_post_code())
    return addr


def get_dob():
    return random_date(datetime(1945, 1, 1, 1, 30, 0),
                       datetime(2009, 1, 1, 14, 30, 0)).date()


def make_row(keys):
    values = [get_name(), get_surname(), get_addr(), get_dob()]
    return dict(zip(keys, values))


def create_contacts_csv(csv_filename, columns, size_in_bytes):
    with open(csv_filename, 'w', newline='') as csv_file:
        csv_writer = csv.DictWriter(csv_file, fieldnames=columns)
        csv_writer.writeheader()
        current_size = 0
        while current_size < size_in_bytes:
            row = make_row(columns)
            csv_writer.writerow(row)
            current_size += getsizeof(row.values())


def make_names(fn):
    with open(fn) as names:
        for name in names:
            NAMES_SET.append(name.strip())


def make_surnames(fn):
    with open(fn) as surnames:
        for surname in surnames:
            SURNAMES_SET.append(surname.strip())


if __name__ == '__main__':
    make_names('NamesDatabases/first names/all.txt')
    make_surnames('NamesDatabases/surnames/all.txt')
    columns = ['first_name',
               'last_name',
               'address',
               'date_of_birth']
    size_in_bytes = 2*10**6 # 2*10**9
    create_contacts_csv('contacts_small.csv', columns, size_in_bytes)
