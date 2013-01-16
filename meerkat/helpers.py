# coding: utf-8
'''
Collection of auxilary helper functions.
'''

def csv_opts(fname, **user_opts):
    '''
    Keep the default csv options and returns user update ones.
    '''
    opts = {
        u'path'     : fname,
        u'header'   : True,
        u'delimiter': u';',
        u'quotechar': u'"',
        u'encoding' : u'utf-8'
    }
    opts.update(user_opts)
    
    return opts


def discover_type_of(column):
    '''
    Tries to determine either the column type is int, float or unicode.
    '''
    types = [int, float, unicode]
    col_type = unicode

    for cast in types:
        if cast is unicode:
            # don't iterate - there are no other options left
            break

        empty_cells = 0
        for cell in column:
            # skip empty cells, but keep track of them
            if not cell.strip():
                empty_cells += 1
                continue

            try:
                cast(cell)
            except ValueError:
                break
        # if run to the end of cells...
        else:
            # ...break types iteration
            col_type = cast
            break

    # return the last successful type
    return col_type if empty_cells != len(column) else unicode

