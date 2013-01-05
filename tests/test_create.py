# coding: utf-8
import meerkat
from nose.tools import raises

def test_create_empty_table():
    t = meerkat.Table()

    assert t.rows_count == 0
    assert t.cols_count == 0

def test_create_table_from_dict():
    data = [
        { 'a': 1, 'b': 2, 'c': 3 },
        { 'a': 4, 'b': 5, 'c': 6 },
        { 'a': 7, 'b': 8, 'c': 9 }
    ]

    t = meerkat.Table(data)

    assert t.rows_count == 3
    assert t.cols_count == 3
    # TODO more asserts here
