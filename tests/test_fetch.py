# coding: utf-8
import meerkat
import types
from nose.tools import raises


def test_fetch_rows():
    data = [
        [ 1,  2,     3   ],
        [ 4,  5,     6   ],
        [ 1,  2,     3   ],
        [ 7,  u'8',  9.0 ]
    ]

    t = meerkat.Table(data)

    assert type(t.rows()) == types.GeneratorType
    assert list(t.rows()) == data


def test_fetch_rows_as_dict():
    data = [
        { u'Gęśl': 1,  u'_gĘśl 1': 2,     u'gesl': 3   },
        { u'Gęśl': 4,  u'_gĘśl 1': 5,     u'gesl': 6   },
        { u'Gęśl': 1,  u'_gĘśl 1': 2,     u'gesl': 3   },
        { u'Gęśl': 7,  u'_gĘśl 1': u'8',  u'gesl': 9.0 }
    ]
        
    t = meerkat.Table(data)

    assert type(t.rows(as_dict=True)) == types.GeneratorType
    assert list(t.rows(as_dict-True)) == data


def test_fetch_columns():
    data = [
        [ 1,  2,     3   ],
        [ 4,  5,     6   ],
        [ 1,  2,     3   ],
        [ 7,  u'8',  9.0 ]
    ]
    columns = [
        [ 1, 4, 1, 7 ],
        [ u"2", u"5", u"2", u"8" ],
        [ 3.0, 6.0, 3.0, 9.0 ]
    ]
    t = meerkat.Table(data)

    assert type(t.columns()) == types.GeneratorType
    assert list(t.columns()) == columns
