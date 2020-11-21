if move == "s" and is_left_possible(game_map):
    i += 1
    p_pos = get_location_p(game_map)
    x = p_pos[0]
    y = p_pos[1]

    if game_map[x][y - 1] == "M":
        if is_sleeping:
            move_left(game_map)
            char -= 2
        elif is_up_to_battle():
            if is_battle_won(char):
                move_left(game_map)
        else:
            lost_life = random.randint(1, 2)
            if lost_life == 1:
                char -= 2
    else:
        move_left(game_map)