def generate_empty_map(nb_rows, nb_cols):
    colums = []
    empty_map = []

    for _ in range(nb_cols):
        colums.append("")
    for _ in range(nb_rows):
        empty_map.append(colums)
    return empty_map

    """
    Return a multi-dimentional list, with given nb of rows and columns.
    All elements should be empty strings --> ""
    :param nb_rows: int representing the nb of to be generated rows
    :param nb_cols: int representing the nb of to be generated columns
    :return: multi-dim list containign empty strings (or None if arguments are negative).
    """
    if nb_rows < 0 or nb_cols < 0:
        return None

    # TODO continue


if __name__ == '__main__':
    pass  # TODO game algorithm
