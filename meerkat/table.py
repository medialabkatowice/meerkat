# coding: utf-8
'''
Main module of the meerkat library implementing Table class
'''


class Table:
    '''
    A simple abstraction over table data structure with
    an easy API for creating, querying and writing tables.
    '''
    def __init__(self):
        pass

    def ___unicode__(self):
        pass

    def rows(self, as_dict=False):
        '''
        Returns a generator to the list of rows. Rows are lists
        of values by default, but can be dicts if as_dict is True
        '''
        pass

    def columns(self):
        '''
        Returns a generator to the list of columns.
        Each column is a list of values.
        '''
        pass

    def row(self, index, as_dict=False):
        '''
        Returns a generator to the list of values of specified row
        or a dict with columns names as keys.
        '''
        pass

    def column(self, index):
        '''
        Returns a generator to the list of values in a specified column.
        '''
        pass

    def value(self, row_index, col_index):
        '''
        Returns a value of a specified cell (row_index, col_index)
        '''
        pass

    def schema(self, new_schema=None):
        '''
        Getter and setter for table's schema. If new_schema is None,
        returns a schema. Otherwise tries to convert all data in the
        table according to new schema and saves new schema. If it
        fails the SchemaError is thrown.
        '''
        pass

    def append(self, row):
        '''
        Appends a new row to the table. The row's length and values types
        have to match table's schema. Otherwise SchemaError is thrown.
        '''
        pass

    def dump(self, **csv_opts):
        '''
        Save table data in csv file. The filename is provided via **csv_opts
        kwargs or during the table initiation.
        '''
        pass
