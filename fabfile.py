from fabric.api import *

def style_test():
    # see the docs for style guidelines
    local("pylint --rcfile .pylintrc meerkat")
    local("pep8 --ignore=E127,E203,E221 meerkat")

def unit_test():
    local("nosetests --rednose")

def test():
    style_test()
    unit_test()
