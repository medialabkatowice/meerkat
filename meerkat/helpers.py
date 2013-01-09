# coding: utf-8

def csv_opts(opts):
    return {}


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

