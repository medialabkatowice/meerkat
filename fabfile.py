from fabric.api import *

def style_test():
    # see the docs for style guidelines
    local("pylint --rcfile .pylintrc meerkat")
    local("pep8 --ignore=E127,E203,E221 meerkat")

def unit_test():
    local("nosetests --rednose --with-coverage")

def test():
    style_test()
    unit_test()

def docs(browser='firefox'):
    local("%s docs/_build/html/index.html &" % browser)

def make_docs():
    with lcd("docs"):
        local("make html")

def update():
    local("git checkout dev")
    local("git pull origin dev")
    make_docs()
    local("git diff")

def push():
    local("git checkout dev")
    local("git status")
    local("git add -p")
    local("git commit")
    local("git push origin dev")
