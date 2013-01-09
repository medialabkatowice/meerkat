# coding: utf-8
import meerkat
from meerkat.errors import NoFileError
from nose.tools import raises
from mock import mock_open
from mock import patch


data = [
    [ 1,  2,     3   ],
    [ 4,  5,     6   ],
    [ 1,  2,     3   ],
    [ 7,  u'8',  9.0 ]
]

dump_01 = u'''
1;"2";3.0
4;"5";6.0
1;"2";3.0
7;"8";9.0
'''.strip()

dump_02 = u'''
"A";"B";"C"
1;"2";3.0
4;"5";6.0
1;"2";3.0
7;"8";9.0
'''.strip()

dump_03 = u'''
*A*|*B*|*C*
1|*2*|3.0
4|*5*|6.0
1|*2*|3.0
7|*8*|9.0
'''.strip()

def test_dump_table():
    csv_opts = {
        u'header'   : False,
        u'delimiter': ';',
        u'quotechar': '"',
        u'encoding' : 'utf-8'
    }
    t = meerkat.Table(data, **csv_opts)
    t.csv_opts['path'] = u'data.csv'

    with patch('__main__.open', create=True) as mo:
        mo.return_value = mock.MagicMock(spec=file)

        t.dump()

        filehandler = mo.return_value.__enter__.return_value
        filehandler.write.assert_called_with(dump_01.encode('utf-8'))


def test_dump_table_with_csv_opts():
    csv_opts = {
        u'path'     : u'data.csv',
        u'header'   : False,
        u'delimiter': ';',
        u'quotechar': '"',
        u'encoding' : 'utf-8'
    }
    t = meerkat.Table(data)

    with patch('__main__.open', create=True) as mo:
        mo.return_value = mock.MagicMock(spec=file)

        t.dump(**csv_opts)

        filehandler = mo.return_value.__enter__.return_value
        filehandler.write.assert_called_with(dump_01.encode('utf-8'))


def test_dump_table_with_header():
    csv_opts = {
        u'path'     : u'data.csv',
        u'header'   : True,
        u'delimiter': ';',
        u'quotechar': '"',
        u'encoding' : 'utf-8'
    }
    t = meerkat.Table(data, labels=["A", "B", "C"])

    with patch('__main__.open', create=True) as mo:
        mo.return_value = mock.MagicMock(spec=file)

        t.dump(**csv_opts)

        filehandler = mo.return_value.__enter__.return_value
        filehandler.write.assert_called_with(dump_02.encode('utf-8'))


def test_dump_table_with_custom_encoding():
    csv_opts = {
        u'path'     : u'data.csv',
        u'header'   : True,
        u'delimiter': ';',
        u'quotechar': '"',
        u'encoding' : 'cp1250'
    }
    t = meerkat.Table(data, labels=["A", "B", "C"])

    with patch('__main__.open', create=True) as mo:
        mo.return_value = mock.MagicMock(spec=file)

        t.dump(**csv_opts)

        filehandler = mo.return_value.__enter__.return_value
        filehandler.write.assert_called_with(dump_02.encode('cp1250'))


def test_dump_table_with_custom_csv_opts():
    csv_opts = {
        u'path'     : u'data.csv',
        u'header'   : True,
        u'delimiter': '|',
        u'quotechar': '*',
        u'encoding' : 'utf-8'
    }
    t = meerkat.Table(data, labels=["A", "B", "C"])

    with patch('__main__.open', create=True) as mo:
        mo.return_value = mock.MagicMock(spec=file)

        t.dump(**csv_opts)

        filehandler = mo.return_value.__enter__.return_value
        filehandler.write.assert_called_with(dump_03.encode('utf-8'))


@raises(NoFileError)
def test_dump_no_file():
    t = meerkat.Table(data)
    t.dump()
