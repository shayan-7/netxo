import sys


def set_no_style():
    sys.stdout.flush()
    sys.stdout.write('\033[0m')

