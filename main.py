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

    empty_map = []
    for _ in range(nb_rows):
        empty_map.append([" " for _ in range(nb_cols)])
    return empty_map


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
        random_row = random.randint(0, nb_rows - 1)
        random_col = random.randint(0, nb_cols - 1)
        if monsters[i] <= nb_rows * nb_cols * 0.2:
            if map[random_row][random_col] == " ":
                map[random_row][random_col] = "M"

        i += 1

    return map


def insert_home(map):
    """
    Inserts a string 'H' on a random position in the given map. This position may not
    contain any monster.
    :param map: a list as is returned by generateEmptyMap()
    :return: the new map (with the added home)
    """
    nb_rows = len(map)
    nb_cols = len(map[0])
    home_in_m = True

    while home_in_m:
        random_row = random.randint(0, nb_rows - 1)
        random_col = random.randint(0, nb_cols - 1)
        if map[random_row][random_col] == " ":
            map[random_row][random_col] = "H"
            home_in_m = False

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
    player_in_m = True

    while player_in_m:
        random_row = random.randint(0, nb_rows - 1)
        random_col = random.randint(0, nb_cols - 1)
        if map[random_row][random_col] == " ":
            map[random_row][random_col] = "P"
            player_in_m = False

    return map


def initialize_game(nb_rows, nb_cols):
    game_map = generate_empty_map(nb_rows, nb_cols)
    insert_monsters_into(game_map)
    insert_player(game_map)
    insert_home(game_map)
    return game_map


def is_battle_won():
    """
    Create a "Pierre-Papier-Ciseaux duel" between the user and a monster.
    :param map: list containing the entire map
    :param char: data-structure holding information about the player's character
    :param monster_position: tuple representing the position of the monster
    :return: the new map (with the eventual changes)
    """

    p_won = 0
    m_won = 0
    i = 0
    while i < 3:
        p_choice = input("Choose 1 (Paper) 2 (Rock) 3 (Scissor): ")
        m_choice = str(random.randint(1, 3))

        while p_choice not in ["1", "2", "3"]:
            p_choice = input("Bnadem, kies 1, 2 of 3: ")

        if p_choice == "1" and m_choice == "2":
            p_won += 1
            print("Paper against rock, you won!")
        elif p_choice == "2" and m_choice == "3":
            p_won += 1
            print("Rock against scissor, you won!")
        elif p_choice == "3" and m_choice == "1":
            p_won += 1
            print("Scissor against paper, you won!")
        elif p_choice == "1" and m_choice == "3":
            m_won += 1
            print("Paper against scissor, you lost!")
        elif p_choice == "2" and m_choice == "1":
            m_won += 1
            print("Rock against paper, you lost!")
        elif p_choice == "3" and m_choice == "2":
            m_won += 1
            print("Scissor against rock, you lost!")

        i += 1

    if m_won < p_won:
        print("You won")
        return True
    elif p_won < m_won:
        print("You lost")
        return False
    else:
        print("It's a draw, fight again")
        return is_battle_won()


def get_nb_monsters(map):
    counter = 0
    for i in range(len(map)):
        for j in range(len(map[0])):
            if map[i][j] == "M":
                counter += 1
    return counter


def is_game_over(char, map):
    return char <= 0 or get_nb_monsters(map) == 0


def get_location_p(game_map):
    for i in range(len(game_map)):
        for j in range(len(game_map[0])):
            if game_map[i][j] == "P":
                return i, j


def get_location_m(game_map):
    for i in range(len(game_map)):
        for j in range(len(game_map[0])):
            if game_map[i][j] == "M":
                return i, j


def is_left_possible(game_map):
    move_l = True
    p_pos = get_location_p(game_map)
    x = p_pos[0]
    y = p_pos[1]
    for i in range(len(game_map)):
        if game_map[i][0] == game_map[x][y]:
            move_l = False
    return move_l


def is_right_possible(game_map):
    move_r = True
    p_pos = get_location_p(game_map)
    x = p_pos[0]
    y = p_pos[1]
    for i in range(len(game_map)):
        if game_map[i][-1] == game_map[x][y]:
            move_r = False
    return move_r


def is_up_possible(game_map):
    move_up = True
    p_pos = get_location_p(game_map)
    x = p_pos[0]
    y = p_pos[1]
    for i in range(len(game_map)):
        if game_map[0][i] == game_map[x][y]:
            move_up = False
    return move_up


def is_down_possible(game_map):
    move_d = True
    p_pos = get_location_p(game_map)
    x = p_pos[0]
    y = p_pos[1]
    for i in range(len(game_map)):
        if game_map[-1][i] == game_map[x][y]:
            move_d = False
    return move_d


def move_left(game_map):
    p_pos = get_location_p(game_map)
    x = p_pos[0]
    y = p_pos[1]
    game_map[x][y-1] = "P"
    game_map[x][y] = " "


def move_right(game_map):
    p_pos = get_location_p(game_map)
    x = p_pos[0]
    y = p_pos[1]
    game_map[x][y+1] = "P"
    game_map[x][y] = " "


def move_up(game_map):
    p_pos = get_location_p(game_map)
    x = p_pos[0]
    y = p_pos[1]
    game_map[x-1][y] = "P"
    game_map[x][y] = " "


def move_down(game_map):
    p_pos = get_location_p(game_map)
    x = p_pos[0]
    y = p_pos[1]
    game_map[x+1][y] = "P"
    game_map[x][y] = " "


def is_sleeping(i):
    return i == 5


def is_up_to_battle():
    fight = True
    ready = input("Are you ready to fight! 1 (yes) or 2 (no): ")
    while ready not in ["1", "2"]:
        ready = input("Are you ready to fight! 1 (yes) or 2 (no): ")
    if ready == "2":
        fight = False
    return fight


def is_m_following():
    return random.randint(1, 10) < 5


if __name__ == '__main__':
    char = 10
    username = input("Username: ")
    game_map = initialize_game(10, 10)
    i = 0
    while not is_game_over(char, game_map):
        print('\n'.join(map(str, game_map)))
        move = input()

        while move not in ["s", "d", "f", "e"]:
            move = input()

        if move == "s" and is_left_possible(game_map):
            i += 1
            p_pos = get_location_p(game_map)
            x = p_pos[0]
            y = p_pos[1]

            if is_sleeping(i) and game_map[x][y-1] == " ":
                print("he is sleeping now")
                i = 0
            elif game_map[x][y-1] == "M":
                if is_sleeping(i):
                    char -= 2
                    i = 0
                    print("A ninja monster killed you while you where sleeping :o")
                elif is_up_to_battle():
                    if is_battle_won():
                        char += 1
                        print("You won :)")
                        move_left(game_map)
                    else:
                        char -= 1
                        print("You lost a life :(")
                else:
                    if is_m_following():
                        print("The monster got you anyway, you lost 2 lives >:)")
                        char -= 2
                    else:
                        print("You got lucky monster was to lazy to follow you!")
            else:
                move_left(game_map)

        if move == "f" and is_right_possible(game_map):
            i += 1
            p_pos = get_location_p(game_map)
            x = p_pos[0]
            y = p_pos[1]
            if is_sleeping(i) and game_map[x][y+1] == " ":
                print("he is sleeping now")
                i = 0
            elif game_map[x][y+1] == "M":
                if is_sleeping(i):
                    char -= 2
                    i = 0
                    print("A ninja monster killed you while you where sleeping :o")
                elif is_up_to_battle():
                    if is_battle_won():
                        char += 1
                        print("You won :)")
                        move_right(game_map)
                    else:
                        char -= 1
                        print("You lost a life :(")
                else:
                    if is_m_following():
                        print("The monster got you anyway, you lost 2 lives >:)")
                        char -= 2
                    else:
                        print("You got lucky monster was to lazy to follow you!")
            else:
                move_right(game_map)

        if move == "e" and is_up_possible(game_map):
            i += 1
            p_pos = get_location_p(game_map)
            x = p_pos[0]
            y = p_pos[1]

            if is_sleeping(i) and game_map[x-1][y] == " ":
                print("he is sleeping now")
                i = 0
            elif game_map[x-1][y] == "M":
                if is_sleeping(i):
                    char -= 2
                    i = 0
                    print("A ninja monster killed you while you where sleeping :o")
                elif is_up_to_battle():
                    if is_battle_won():
                        char += 1
                        print("You won :)")
                        move_up(game_map)
                    else:
                        char -= 1
                        print("You lost a life :(")
                else:
                    if is_m_following():
                        print("The monster got you anyway, you lost 2 lives >:)")
                        char -= 2
                    else:
                        print("You got lucky monster was to lazy to follow you!")
            else:
                move_up(game_map)

        if move == "d" and is_down_possible(game_map):
            i += 1
            p_pos = get_location_p(game_map)
            x = p_pos[0]
            y = p_pos[1]

            if is_sleeping(i) and game_map[x+1][y] == " ":
                print("he is sleeping now")
                i = 0
            elif game_map[x+1][y] == "M":
                if is_sleeping(i):
                    char -= 2
                    i = 0
                    print("A ninja monster killed you while you where sleeping :o")
                elif is_up_to_battle():
                    if is_battle_won():
                        char += 1
                        print("You won :)")
                        move_down(game_map)
                    else:
                        char -= 1
                        print("You lost a life :(")
                else:
                    if is_m_following():
                        print("The monster got you anyway, you lost 2 lives >:)")
                        char -= 2
                    else:
                        print("You got lucky monster was to lazy to follow you!")

            else:
                move_down(game_map)

        print(f"{char} lives left")

    if char == 0:
        print("You lost\nGame over")

    elif get_nb_monsters(game_map) == 0:
        print("You won\nGame over")
