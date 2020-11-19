import random


def generate_empty_map(nb_rows, nb_cols):
    """
    Return a multi-dimentional list, with given nb of rows and columns.
    All elements should be empty strings --> ""
    :param nb_rows: int representing the nb of to be generated rows
    :param nb_cols: int representing the nb of to be generated columns
    :return: multi-dim list containign empty strings (or None if arguments are negative).
    """
    if nb_rows < 0 or nb_cols < 0:
        return None

    columns = []
    empty_map = []

    for _ in range(nb_cols):
        columns.append("")
    for _ in range(nb_rows):
        empty_map.append(columns)

    return empty_map



   # TODO map_dimension weg doen


def insert_monsters_into(map: list):
    """
    Insert monsters randomly in positions of given map (list) by changing the value at
    that position into
    the string: 'M'. Every position of the map has 20% chance to get a monster.
    :param map: a list as is returned by generateEmptyMap()
    :return: the new map (with the added monsters)
    """
    assert len(map) > 0

    nb_rows = len(map)
    nb_cols = len(map[0])
    monsters = random.sample([*range(100)], nb_rows * nb_cols)
    i = 0

    while i < nb_rows * nb_cols:
        if monsters[i] <= nb_rows * nb_cols * 0.2:
            map[random.randint(0, nb_rows-1)][random.randint(0, nb_cols-1)] = "M"
        i += 1

    return map



def make_home(map):
    """
    Inserts a string 'H' on a random position in the given map. This position may not
    contain any monster.
    :param map: a list as is returned by generateEmptyMap()
    :return: the new map (with the added home)
    """
    nb_rows = len(map)
    nb_cols = len(map[0])

    if map[random.randint(0, nb_rows-1)][random.randint(0, nb_cols-1)] != "M" in map:
        map[random.randint(0, nb_rows - 1)][random.randint(0, nb_cols - 1)] = "H"
    return map


def insert_player(map):
    """
    Inserts a string 'P' on a random position in the given map. This position may not
    contain any monster.
    :param map: a list as is returned by generateEmptyMap()
    :return: the new map (with the added player)
    """

    nb_rows = len(map)
    nb_cols = len(map[0])

    map[random.randint(0, nb_rows-1)][random.randint(0, nb_cols-1)] = "P"
    return map





    #TODO check with Adam




if __name__ == '__main__':
    pass  # TODO game algorithm

