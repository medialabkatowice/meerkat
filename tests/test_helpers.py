# coding: utf-8
# import utils
import meerkat.helpers as utils
from nose.tools import raises

# utils.slugify tests
def test_basic_slugify():
    text = utils.slugify(u'Zażółć Gęślą Jaźń')
    assert u'zazolc-gesla-jazn' == text

def test_basic_slugify_with_str_argument():
    text = utils.slugify('Zażółć Gęślą Jaźń')
    assert u'zazolc-gesla-jazn' == text

def test_basic_slugify_with_numeric_argument():
    text = utils.slugify(u'1234567890')
    assert u'1234567890' == text

def test_slugify_with_multiple_nonalphanums_in_row():
    text = utils.slugify(u'Zażółć, Gęślą_Jaźń')
    assert u'zazolc-gesla-jazn' == text

def test_slugify_with_nonalphanums_at_front_and_back():
    text = utils.slugify(u'  Zażółć, (Gęślą_Jaźń)')
    assert u'zazolc-gesla-jazn' == text

def test_slugify_unicode_output():
    text = utils.slugify(u'1234567890')
    assert type(text) == unicode


# utils.get_opts tests
def test_get_opts_with_empty_arguments():
    a, b, c = utils.get_opts({})
    assert a == {'delimiter': ';', 'quotechar': '"'}
    assert b == True
    assert c == 0

def test_get_opts_overriding_defaults():
    opts = {
        'delimiter': ',', 
        'quotechar': "'",
        'header'   : False, 
        'how_deep' : 1
    }
    a, b, c = utils.get_opts(opts)
    assert a == {'delimiter': ',', 'quotechar': "'"}
    assert b == False
    assert c == 1

@raises(TypeError)
def test_get_opts_with_no_arguments():
    utils.get_opts()


# utils.discover_type_of tests
def test_discover_type_of_for_ints():
    column = ['1', '2', '3', '4', '5']
    assert utils.discover_type_of(column) == int

def test_discover_type_of_for_floats():
    column = ['1.1', '2.2', '3.3', '4.4', '5.5']
    assert utils.discover_type_of(column) == float

def test_discover_type_of_for_strings():
    column = ['a', 'b', 'c']
    assert utils.discover_type_of(column) == unicode

def test_discover_type_of_for_unicodes():
    column = [u'a', u'b', u'c']
    assert utils.discover_type_of(column) == unicode

def test_discover_type_of_with_some_empty_cells():
    column = [u'1', u'', u'3']
    assert utils.discover_type_of(column) == int

def test_discover_type_of_with_all_empty_cells():
    column = [u'', u'', u'']
    assert utils.discover_type_of(column) == unicode
