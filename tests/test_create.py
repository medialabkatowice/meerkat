# coding: utf-8
import meerkat
from nose.tools import raises


def test_create_empty_table():
    t = meerkat.Table()

    assert t.rows_count == 0
    assert t.cols_count == 0
    assert t.schema == []


def test_create_empty_table_with_schema():
    test_schema = [
        {
            u'label': u'Gęśl',
            u'type' : int
        },
        {
            u'label': u'_gĘśl 1',
            u'type' : unicode
        },
        {
            u'label': u'gesl',
            u'type' : float
        }
    ]
    t = meerkat.Table([], schema=test_schema)

    assert t.rows_count == 0
    assert t.cols_count == 3
    assert t.schema == [
        {
            u'label': u'Gęśl',
            u'slug' : u'gesl',
            u'index': 0,
            u'type' : int
        },
        {
            u'label': u'_gĘśl 1',
            u'slug' : u'gesl-1',
            u'index': 1,
            u'type' : unicode
        },
        {
            u'label': u'gesl',
            u'slug' : u'gesl',
            u'index': 2,
            u'type' : float
        }
    ]


def test_create_table_from_dict():
    data = [
        { u'Gęśl': 1,  u'_gĘśl 1': 2,     u'gesl': 3   },
        { u'Gęśl': 4,  u'_gĘśl 1': 5,     u'gesl': 6   },
        { u'Gęśl': 1,  u'_gĘśl 1': 2,     u'gesl': 3   },
        { u'Gęśl': 7,  u'_gĘśl 1': u'8',  u'gesl': 9.0 }
    ]

    t = meerkat.Table(data)

    assert t.rows_count == 4
    assert t.cols_count == 3
    assert t.schema == [
        {
            u'label': u'Gęśl',
            u'slug' : u'gesl',
            u'index': 0,
            u'type' : int
        },
        {
            u'label': u'_gĘśl 1',
            u'slug' : u'gesl-1',
            u'index': 1,
            u'type' : unicode
        },
        {
            u'label': u'gesl',
            u'slug' : u'gesl',
            u'index': 2,
            u'type' : float
        }
    ]


def test_create_table_from_list():
    data = [
        [ 1,  2,     3   ],
        [ 4,  5,     6   ],
        [ 1,  2,     3   ],
        [ 7,  u'8',  9.0 ]
    ]

    t = meerkat.Table(data)

    assert t.rows_count == 4
    assert t.cols_count == 3
    assert t.schema == [
        {
            u'label': u'Column 1',
            u'slug' : u'column-1',
            u'index': 0,
            u'type' : int
        },
        {
            u'label': u'Column 2',
            u'slug' : u'column-2',
            u'index': 1,
            u'type' : unicode
        },
        {
            u'label': u'Column 3',
            u'slug' : u'column-3',
            u'index': 2,
            u'type' : float
        }
    ]
