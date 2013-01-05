# coding: utf-8

def slugify(text):
    import re
    non_alpha = re.compile(r'\W+')
    chars = { 
        u'ą': u'a', u'ż': u'z', u'ś': u's',
        u'ź': u'z', u'ę': u'e', u'ć': u'c',
        u'ń': u'n', u'ó': u'o', u'ł': u'l'
    }

    if type(text) is str:
      text = text.decode('utf-8')
    else:
      text = unicode(text)

    text = text.lower()
    for k, v in chars.items():
        text = text.replace(k, v)
    text = text.replace('_', '-')
    text = non_alpha.sub('-', text).strip('-')

    return text


def get_opts(opts):
    csv_opts = {
        'delimiter': opts.get('delimiter', ';'),
        'quotechar': opts.get('quotechar', '"')
    }
    has_header = opts.get('header', True)
    how_deep   = opts.get('how_deep', 0)

    return (csv_opts, has_header, how_deep)


def discover_type_of(column):
    types = [int, float, unicode]

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
            except:
                break
        # if run to the end of cells... 
        else:
            # ...break types iteration
            break

    # return the last successful type
    return cast if empty_cells != len(column) else unicode

