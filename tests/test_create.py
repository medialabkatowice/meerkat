# coding: utf-8
import meerkat
from nose.tools import raises
from mock import mock_open
from mock import patch


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
    assert list(t.schema()) == [
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
    assert t.csv_opts == {}


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
    assert list(t.schema()) == [
        {
            u'label': u'Column 1',
            u'type' : int
        },
        {
            u'label': u'Column 2',
            u'type' : unicode
        },
        {
            u'label': u'Column 3',
            u'type' : float
        }
    ]
    assert t.csv_opts == {}


def test_create_from_file():
    data = u'''# data file example
    "Gęśl";"_gĘśl 1";"gesl"
    1;2;3
    4;5;6

    1;2;3

    # special row
    7;"X";9.0
    '''.encode('utf-8')

    with patch('__main__.open', mock_open(read_data=data), create=True) as m:
        t = meerkat.Table('data.csv')

        assert m.assert_called_once_with('data.csv', 'r')

        assert t.rows_count == 4
        assert t.cols_count == 3
        assert list(t.schema()) == [
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
        assert t.csv_opts == {
            u'path'     : 'data.csv',
            u'header'   : True,
            u'delimiter': u';',
            u'quotechar': u'"',
            u'encoding' : u'utf-8'
        }


def test_create_empty_table():
    t = meerkat.Table()

    assert t.rows_count == 0
    assert t.cols_count == 0
    assert list(t.schema()) == []
    assert t.csv_opts == {}


def test_create_with_empty_file():
    t = meerkat.Table('data.csv')

    assert t.rows_count == 0
    assert t.cols_count == 0
    assert list(t.schema()) == []
    assert t.csv_opts == {
        u'path'     : 'data.csv',
        u'header'   : True,
        u'delimiter': u';',
        u'quotechar': u'"',
        u'encoding' : u'utf-8'
    }


def test_create_empty_table_with_labels_and_types():
    labels = [ u'Gęśl', u'_gĘśl 1', u'gesl' ]
    types  = [ int, unicode, float ]

    t = meerkat.Table([], labels=labels, types=types)

    assert t.rows_count == 0
    assert t.cols_count == 3
    assert list(t.schema()) == [
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
    assert t.csv_opts == {}


def test_create_from_file_with_custom_labels():
    data = u'''# data file example
    "Gęśl";"_gĘśl 1";"gesl"
    1;2;3
    4;5;6

    1;2;3

    # special row
    7;"X";9.0
    '''.encode('utf-8')
    labels = [u'Jaźń', u'_jAźń 1', u'jazn']

    with patch('__main__.open', mock_open(read_data=data), create=True) as m:
        t = meerkat.Table('data.csv', labels=labels)

        assert m.assert_called_once_with('data.csv', 'r')

        assert t.rows_count == 4
        assert t.cols_count == 3
        assert list(t.schema()) == [
            {
                u'label': u'Jaźń',
                u'type' : int
            },
            {
                u'label': u'_jAźń 1',
                u'type' : unicode
            },
            {
                u'label': u'jazn',
                u'type' : float
            }
        ]
        assert t.csv_opts == {
            u'path'     : 'data.csv',
            u'header'   : True,
            u'delimiter': u';',
            u'quotechar': u'"',
            u'encoding' : u'utf-8'
        }


def test_create_table_with_custom_types():
    data = [
        [ 1,  2,     3   ],
        [ 4,  5,     6   ],
        [ 1,  2,     3   ],
        [ 7,  u'X',  9.0 ]
    ]
    types = [ unicode, unicode, float ]

    t = meerkat.Table(data, types=types)

    assert list(t.schema()) == [
        {
            u'label': u'Column 1',
            u'type' : unicode
        },
        {
            u'label': u'Column 2',
            u'type' : unicode
        },
        {
            u'label': u'Column 3',
            u'type' : float
        }
    ]


def test_create_from_file_no_header():
    data = u'''# data file example
    1;2;3
    4;5;6

    1;2;3

    # special row
    7;"X";9.0
    '''.encode('utf-8')

    with patch('__main__.open', mock_open(read_data=data), create=True) as m:
        t = meerkat.Table('data.csv', csv_header=False)

        assert m.assert_called_once_with('data.csv', 'r')

        assert t.rows_count == 4
        assert t.cols_count == 3
        assert list(t.schema()) == [
            {
                u'label': u'Column 1',
                u'type' : int
            },
            {
                u'label': u'Column 2',
                u'type' : unicode
            },
            {
                u'label': u'Column 3',
                u'type' : float
            }
        ]
        assert t.csv_opts == {
            u'path'     : 'data.csv',
            u'header'   : False,
            u'delimiter': u';',
            u'quotechar': u'"',
            u'encoding' : u'utf-8'
        }


def test_create_from_file_no_header_with_custom_labels():
    data = u'''# data file example
    1;2;3
    4;5;6

    1;2;3

    # special row
    7;"X";9.0
    '''.encode('utf-8')
    labels = [u'Jaźń', u'_jAźń 1', u'jazn']

    with patch('__main__.open', mock_open(read_data=data), create=True) as m:
        t = meerkat.Table('data.csv', labels=labels, csv_header=False)

        assert m.assert_called_once_with('data.csv', 'r')

        assert t.rows_count == 4
        assert t.cols_count == 3
        assert list(t.schema()) == [
            {
                u'label': u'Jaźń',
                u'type' : int
            },
            {
                u'label': u'_jAźń 1',
                u'type' : unicode
            },
            {
                u'label': u'jazn',
                u'type' : float
            }
        ]
        assert t.csv_opts == {
            u'path'     : 'data.csv',
            u'header'   : True,
            u'delimiter': u';',
            u'quotechar': u'"',
            u'encoding' : u'utf-8'
        }


def test_create_from_file_with_custom_csv_opts():
    data = u'''# data file example
    *Gęśl*|*_gĘśl 1*|*gesl*
    1|2|3
    4|5|6

    1|2|3

    # special row
    7|*X*|9.0
    '''.encode('utf-8')

    with patch('__main__.open', mock_open(read_data=data), create=True) as m:
        t = meerkat.Table('data.csv', delimiter='|', quotechar='*')

        assert m.assert_called_once_with('data.csv', 'r')

        assert t.rows_count == 4
        assert t.cols_count == 3
        assert list(t.schema()) == [
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
        assert t.csv_opts == {
            u'path'     : 'data.csv',
            u'header'   : True,
            u'delimiter': u'|',
            u'quotechar': u'*',
            u'encoding' : u'utf-8'
        }


def test_create_from_file_with_different_encoding():
    data = u'''# data file example
    "Gęśl";"_gĘśl 1";"gesl"
    1;2;3
    4;5;6

    1;2;3

    # special row
    7;"X";9.0
    '''.encode('cp1250')

    with patch('__main__.open', mock_open(read_data=data), create=True) as m:
        t = meerkat.Table('data.csv', encoding='cp1250')

        assert m.assert_called_once_with('data.csv', 'r')

        assert t.rows_count == 4
        assert t.cols_count == 3
        assert list(t.schema()) == [
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
        assert t.csv_opts == {
            u'path'     : 'data.csv',
            u'header'   : True,
            u'delimiter': u';',
            u'quotechar': u'"',
            u'encoding' : u'cp1250'
        }


def test_create_unicode_as_default_type():
    labels = [u'Jaźń', u'_jAźń 1', u'jazn']

    t = meerkat.Table(labels=labels)

    assert list(t.schema()) == [
        {
            u'label': u'Jaźń',
            u'type' : unicode
        },
        {
            u'label': u'_jAźń 1',
            u'type' : unicode
        },
        {
            u'label': u'jazn',
            u'type' : unicode
        }
    ]

@raises(SchemaError)
def test_create_with_duplicated_column_labels():
    labels = [ u'zażółć', u'gęślą', u'zażółć' ]

    t = meerkat.Table(labels=labels)



