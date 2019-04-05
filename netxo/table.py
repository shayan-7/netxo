import shutil


class XOTable:
    table_string = '''
    %(c00)s | %(c01)s |  %(c02)s

     -----  +  -----  +  -----

    %(c10)s | %(c11)s |  %(c12)s

     -----  +  -----  +  -----

    %(c20)s | %(c21)s |  %(c22)s
    '''
    __coordinates__ = {
        'c00': (chr(32) * 7),
        'c01': (chr(32) * 7),
        'c02': (chr(32) * 7),
        'c10': (chr(32) * 7),
        'c11': (chr(32) * 7),
        'c12': (chr(32) * 7),
        'c20': (chr(32) * 7),
        'c21': (chr(32) * 7),
        'c22': (chr(32) * 7),
    }
    printed = False

    def __init__(self):
        self.table_string % self.__coordinates__
        self.signature = '\U0001F389'
        self.rows = self.table_string.count('\n') + 3
        self.columns = len(self.table_string.split('\n')[1])

    @property
    def current(self):
        return self.table_string % self.__coordinates__

    @property
    def coordinates(self):
        return self.__coordinates__

    @coordinates.setter
    def coordinates(self, index):
        index = 'c' + index
        self.__coordinates__[index] = self.signature.center(6)

    def print_center(self):
        columns = shutil.get_terminal_size().columns + 7
        if not self.printed:
            print(self.table_string % self.__coordinates__)
            self.printed = True
            return

        print('\033[A' * self.rows)
        print(self.table_string % self.__coordinates__)

