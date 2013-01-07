.. meerkat documentation master file, created by
   sphinx-quickstart on Mon Jan  7 08:15:37 2013.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

meerkat - tables simplified
===================================

meerkat is a simple abstraction over a table data structure. It's being
developed for the educational purpose with the audience being python beginners.
During multiple workshops it turned out that csv module is too low-level (and
doesn't provide the table abstraction) and Pandas is too sophisticated
for the beginners. 

Table object
============

The main data structure in meerkat module is a Table class. Table objects can
be created of:

- list of dicts
- list of lists
- csv files (of different dialects)
- as an empty table (with optionally associated csv file for final dump)

and written to the csv file.

Table constructor
------------------

.. method:: Table(data_source=None, labels=[], types=[], \*\*csv_opts) 

   Table constructor can initialized in four different ways depending on data
   parameter's type:

   - from *list of dicts* where each dict is a single row and keys represent
     columns names:
     ::
      [
          {
              u'column 1': 1,
              u'column 2': 2,
              u'column 3': 3
          },
          {
              u'column 1': 4,
              u'column 2': 5,
              u'column 3': 6
          }
      ]

     Each dict in the data list has to have the same keys (all columns). If
     some value is not present None should be provided:
     ::
      [
          {
              u'column 1': 1,
              u'column 2': None,
              u'column 3': 3
          },
          {
              u'column 1': 4,
              u'column 2': 5,
              u'column 3': None
          }
      ]


   - from *list of lists* where each list is a single row:
     ::
      [
          [ 1, 2, 3 ],
          [ 4, 5, 6 ]
      ]
     
     By default all columns names will be set to 'Column 1', 'Column 2'
     (starting from 1!). This behaviour can be overwritten with *labels*
     parameter.

   - from *csv file*:
     ::
      t = Table('data.csv')

     Some csv related options (*\*\*csv_opts*) are available (see below):
     
   - with no data provided in two possible ways:
     ::
      t = Table()
     
     or with a name of file to be created while dumping the table data:
     ::
      t = Table('data.csv')

     In both cases Table object is empty assuming there is no such file in the
     second call.  If so, the filename will be stored in for future data dump.
     As with reading data from file, the additional csv_opts kwargs are
     available.

   Table constructor takes several optional arguments:

   - *labels* is a list of strings (or unicodes) to be used as column labels (and derived column slugs)
   - *types* is a list of python types to be used for storing data in each
     column. Types available are *int*, *float* and *unicode*. It's especially
     helpfull when a numeric values are string labels and should be treated as
     such (e.g. personal ID).
   - *\*\*csv_opts* is a collection of csv related arguments (here shown with defaults):
     ::
      {
          u'header'   : True,     # whether file has a header row or not
          u'delimiter': u';',     # csv module delimiter argument
          u'quotechar': u'"',     # csv module quotechar argument
          u'encoding' : u'utf-8'  # what is the file encoding
      }
     
     These kwargs are available for both reading data from file and creating
     an empty *Table* with a file provided for future dumps.

Table attributes
----------------

.. attribute:: rows_count

   Number of rows in the table


.. attribute:: cols_count

   Number of columns in the table


.. attribute:: schema

   List containing basic information about columns in the table. Each column is described by a dict:
   ::
    [
        {
            u'label': u'Full name of the column',
            u'slug' : u'full-name-of-the-column',
            u'index': 0,
            u'type' : unicode
        },
        {
            u'label': u'Full name of another column',
            u'slug' : u'full-name-of-another-column',
            u'index': 1,
            u'type' : float
        }
    ]


.. attribute:: csv_opts

   All information needed to create a csv file to write the table data. The csv_opts is such a dict:
   ::
    {
        u'path'     : '/path/to/file.csv',
        u'header'   : True,
        u'delimiter': u';',
        u'quotechar': u'"',
        u'encoding' : u'utf-8'
    }


Indices and tables
==================

* :ref:`genindex`
* :ref:`search`

