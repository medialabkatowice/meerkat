# coding: utf-8
import meerkat
from meerkat.errors import SchemaError
from nose.tools import raises

def test_modify_schema():
    labels = [ u'zażółć', u'gęslą', u'jaźń' ]
    types  = [ int      , float   , unicode ]

    new_schema = [
        {
            u'label': u'Kot Wincenty',
            u'type' : unicode
        },
        {
            u'label': u'Pies Alojzy',
            u'type' : int
        },
        {
            u'label': u'Mysz Bonifacy',
            u'type' : float
        }
    ]

    t = meerkat.Table(labels=labels, types=types)
    t.schema(new_schema)

    assert list(t.schema()) == [
        {
            u'label': u'Kot Wincenty',
            u'label': u'kot-wincenty',
            u'type' : unicode
        },
        {
            u'label': u'Pies Alojzy',
            u'label': u'pies-alojzy',
            u'type' : int
        },
        {
            u'label': u'Mysz Bonifacy',
            u'label': u'mysz-bonifacy',
            u'type' : float
        }
    ]


@raises(SchemaError)
def test_modify_schema_with_wrong_types():
    labels = [ u'zażółć', u'gęslą', u'jaźń' ]
    data = [
        [ 1,  2,     3   ],
        [ 4,  5,     6   ],
        [ 1,  2,     3   ],
        [ 7,  u'X',  9.0 ]
    ]

    new_schema = [
        {
            u'label': u'Kot Wincenty',
            u'type' : int
        },
        {
            u'label': u'Pies Alojzy',
            u'type' : int
        },
        {
            u'label': u'Mysz Bonifacy',
            u'type' : float
        }
    ]

    t = meerkat.Table(data, labels=labels)
    t.schema(new_schema)


@raises(SchemaError)
def test_modify_schema_with_different_length():
    labels = [ u'zażółć', u'gęslą', u'jaźń' ]
    types  = [ int      , float   , unicode ]

    new_schema = [
        {
            u'label': u'Kot Wincenty',
            u'type' : unicode
        },
        {
            u'label': u'Mysz Bonifacy',
            u'type' : float
        }
    ]

    t = meerkat.Table(labels=labels, types=types)
    t.schema(new_schema)


@raises(SchemaError)
def test_modify_schema_with_duplicated_labels():
    labels = [ u'zażółć', u'gęslą', u'jaźń' ]
    types  = [ int      , float   , unicode ]

    new_schema = [
        {
            u'label': u'Kot Wincenty',
            u'type' : unicode
        },
        {
            u'label': u'Kot Wincenty',
            u'type' : float
        }
    ]

    t = meerkat.Table(labels=labels, types=types)
    t.schema(new_schema)


def test_modify_append_row():
    data = [
        [ 1,  2,     3   ],
        [ 4,  5,     6   ],
        [ 7,  u'X',  9.0 ]
    ]
    new_row  = [ 1, u'Y', 3.0 ]

    t = meerkat.Table(data)
    t.append(new_row)

    assert list(t.rows()) == [
        [ 1, u'2', 3.0 ],
        [ 4, u'5', 6.0 ],
        [ 7, u'X', 9.0 ]
        [ 1, u'Y', 3.0 ]
    ]
    assert t.rows_count == 4
    assert t.cols_count == 3


@raises(SchemaError)
def test_modify_append_too_long_row():
    data = [
        [ 1,  2,     3   ],
        [ 4,  5,     6   ],
        [ 7,  u'X',  9.0 ]
    ]
    new_row  = [ 1, u'Y', 3.0, u'Z' ]

    t = meerkat.Table(data)
    t.append(new_row)


@raises(SchemaError)
def test_modify_append_too_short_row():
    data = [
        [ 1,  2,     3   ],
        [ 4,  5,     6   ],
        [ 7,  u'X',  9.0 ]
    ]
    new_row  = [ 1, u'Y' ]

    t = meerkat.Table(data)
    t.append(new_row)


@raises(SchemaError)
def test_modify_append_row_with_wrong_types():
    data = [
        [ 1,  2,     3   ],
        [ 4,  5,     6   ],
        [ 7,  u'X',  9.0 ]
    ]
    new_row  = [ 3.14, 10, u'Z' ]

    t = meerkat.Table(data)
    t.append(new_row)
