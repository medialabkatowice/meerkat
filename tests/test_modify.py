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
