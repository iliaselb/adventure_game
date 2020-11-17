from main import *

######################
# generate_empty_map #
######################
assert generate_empty_map(2, 2) == \
    [["", ""], ["", ""]]
assert generate_empty_map(5, 5) == \
    [["", "", "", "", ""],
     ["", "", "", "", ""],
     ["", "", "", "", ""],
     ["", "", "", "", ""],
     ["", "", "", "", ""]]
assert generate_empty_map(-1, -1) is None
