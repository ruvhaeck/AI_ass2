import Map

def h(pos_a: list[int], pos_b:list[int]):
    return abs(pos_a[0] - pos_b[0]) + abs(pos_a[1] - pos_b[1])

def get_valid_neighbours(pos: list[int], map):
    neighbours = []
    if pos[0] > 0 and map[pos[0]-1][pos[1]] != -1:   # check if the position is not a left wall
        neighbours.append([pos[0]-1, pos[1]])
    if pos[0] < len(map) - 1 and map[pos[0]+1][pos[1]] != -1:  # check if the position is not a right wall
        neighbours.append([pos[0]+1, pos[1]])
    if pos[1] > 0 and map[pos[0]][pos[1]-1] != -1:  # check if the position is not a top wall
        neighbours.append([pos[0], pos[1]-1])
    if pos[1] < len(map[0]) - 1 and map[pos[0]][pos[1]+1] != -1:    # check if the position is not a bottom wall
        neighbours.append([pos[0], pos[1]+1])
    return neighbours


def a_star(start_pos: list[int], end_pos: list[int], map, obj: Map.Map_Obj):
    path = []
    frontier = []
    expand = start_pos
    # dict with as key the positions and value 'cost so far'
    g = {tuple(obj.get_start_pos()): 0}  # cost so far 
    came_from = {}
    while expand != end_pos:
        neighbours = get_valid_neighbours(expand, map)
        for neighbour in neighbours:
            if tuple(neighbour) not in list(g.keys()):
                g[tuple(neighbour)] = g[tuple(expand)] + obj.get_cell_value(neighbour)
                frontier.append(neighbour)
                came_from[tuple(neighbour)] = tuple(expand)
        frontier.sort(key=lambda x: h(x, end_pos) + g[tuple(x)])
        prev_expand = expand
        expand = frontier.pop(0)
    pos = tuple(end_pos)
    while pos != tuple(start_pos):
        pos = came_from[tuple(pos)]
        path.append(pos)
    del(path[len(path)-1])

    return path


task = 4
if task == 1:
    obj = Map.Map_Obj(task=1)
    map, map_string = obj.read_map("Samfundet_map_1.csv")
    path = a_star(obj.get_start_pos(), obj.get_end_goal_pos(), map, obj)
    for pos in path:
        obj.set_cell_value(pos, 3)
    obj.show_map()
elif task == 2:
    obj = Map.Map_Obj(task=2)
    map, map_string = obj.read_map("Samfundet_map_1.csv")
    path = a_star(obj.get_start_pos(), obj.get_end_goal_pos(), map, obj)
    for pos in path:
        obj.set_cell_value(pos, 3)
    obj.show_map()
elif task == 3:
    obj = Map.Map_Obj(task=3)
    map, map_string = obj.read_map("Samfundet_map_2.csv")
    path = a_star(obj.get_start_pos(), obj.get_end_goal_pos(), map, obj)

    for pos in path:
        obj.set_cell_value(pos, 3)
    obj.show_map()
elif task == 4:
    obj = Map.Map_Obj(task=4)
    map, map_string = obj.read_map("Samfundet_map_2.csv")

    path = a_star(obj.get_start_pos(), obj.get_end_goal_pos(), map, obj)
    print("finished, path:", path)

    for pos in path:
        obj.set_cell_value(pos, 3)
    obj.show_map()