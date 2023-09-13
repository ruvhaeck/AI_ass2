import Map

def h(pos_a: list[int], pos_b:list[int]):
    return abs(pos_a[0] - pos_b[0]) + abs(pos_a[1] - pos_b[1])


def a_star(start_pos: list[int], end_pos: list[int], map):
    path = []
    frontier = []
    expand = start_pos
    # dict with as key the positions and value 'cost so far'
    g = {}  # cost so far 

    return path

obj = Map.Map_Obj(task=1)
map, map_string = obj.read_map("Samfundet_map_1.csv")
obj.print_map(map_to_print=map)
obj.show_map(themap=map_string)