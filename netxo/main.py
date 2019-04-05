from .table import XOTable
from .helpers import set_no_style


def main():

    xo = XOTable()

    while True:
        xo.print_center()

        index = input('\033[32;1m\033[K> What is your index? \033[34;1m')
        set_no_style()
        if index == 'cancel':
            break

        xo.coordinates = index

