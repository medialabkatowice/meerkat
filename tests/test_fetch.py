# coding: utf-8
import meerkat
import types
from nose.tools import raises

data = [
    [ 1,  2,     3   ],
    [ 4,  5,     6   ],
    [ 1,  2,     3   ],
    [ 7,  u'8',  9.0 ]
]


def test_fetch_rows():
    t = meerkat.Table(data)

    assert type(t.rows()) == types.GeneratorType
    assert list(t.rows()) == data


def test_fetch_rows_as_dict():
    t = meerkat.Table(data)

    assert type(t.rows(as_dict=True)) == types.GeneratorType
    assert list(t.rows(as_dict-True)) == data


def test_fetch_columns():
    columns = [
        [ 1, 4, 1, 7 ],
        [ u"2", u"5", u"2", u"8" ],
        [ 3.0, 6.0, 3.0, 9.0 ]
    ]
    t = meerkat.Table(data)

    assert type(t.columns()) == types.GeneratorType
    assert list(t.columns()) == columns


def test_fetch_row():
    row = [ 1, u'2', 3.0 ]

    t = meerkat.Table(data)

    assert type(t.row(0)) == types.GeneratorType
    assert list(t.row(0)) == row


def test_fetch_column_by_index():
    column = [ 1, 4, 1, 7 ]

    t = meerkat.Table(data)

    assert type(t.column(0)) == types.GeneratorType
    assert list(t.column(0)) == column


def test_fetch_column_by_name():
    column = [ 1, 4, 1, 7 ]

    t = meerkat.Table(data)

    assert type(t.column(u'Column 1')) == types.GeneratorType
    assert list(t.column(u'Column 1')) == column


def test_fetch_column_by_slug():
    column = [ 1, 4, 1, 7 ]

    t = meerkat.Table(data)

    assert type(t.column(u'column-1')) == types.GeneratorType
    assert list(t.column(u'column-1')) == column


def test_fetch_value_by_index():
    t = meerkat.Table(data)

    assert type(t.value(0, 0)) == types.GeneratorType
    assert list(t.value(0, 0)) == 1


def test_fetch_value_by_name():
    t = meerkat.Table(data)

    assert type(t.value(0, u'Column 1')) == types.GeneratorType
    assert list(t.value(0, u'Column 1')) == 1


def test_fetch_value_by_slug():
    t = meerkat.Table(data)

    assert type(t.value(0, u'column-1')) == types.GeneratorType
    assert list(t.value(0, u'column-1')) == 1


