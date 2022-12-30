from aocd import lines
from utils import split_lines, Vec2, CharGrid


grid_data, [code] = split_lines(lines)
grid = CharGrid(grid_data, pad=" ")
pos1, dir1 = Vec2(0, grid_data[0].index(".")), Vec2(0, 1)
pos2, dir2 = pos1, dir1
code += "R0L"
i = 0


# My map looks like this:
#   |1|2|
#   |4|
# |6|7|
# |9|

R, D, L, U = Vec2(0, 1), Vec2(1, 0), Vec2(0, -1), Vec2(-1, 0)
edge_pairs = [
    {(1, L), (6, L)},
    {(4, L), (6, U)},
    {(2, R), (7, R)},
    {(4, R), (2, D)},
    {(9, R), (7, D)},
    {(1, U), (9, L)},
    {(2, U), (9, D)},
]
edge_len = 50


def get_face_num(pos: Vec2):
    return (grid.ncols // edge_len) * (pos.x // edge_len) + (pos.y // edge_len)


def get_face_pos(face_num: int):
    face_row = face_num // (grid.ncols // edge_len)
    face_col = face_num % (grid.ncols // edge_len)
    return Vec2(edge_len * face_row, edge_len * face_col)


def get_offset_amt(pos: Vec2, dir: Vec2):
    match dir:
        case 0, 1:  # R
            return pos.x % edge_len
        case 1, 0:  # D
            return (-pos.y - 1) % edge_len
        case 0, -1:  # L
            return (-pos.x - 1) % edge_len
        case -1, 0:  # U
            return pos.y % edge_len


def get_offset_vec(amt: int, dir: Vec2):
    match dir:
        case 0, 1:  # R
            return Vec2(edge_len - 1 - amt, edge_len - 1)
        case 1, 0:  # D
            return Vec2(edge_len - 1, amt)
        case 0, -1:  # L
            return Vec2(amt, 0)
        case -1, 0:  # U
            return Vec2(0, edge_len - 1 - amt)


while i < len(code):
    j = len(code)
    for rl in "RL":
        try:
            j = min(j, code.index(rl, i))
        except ValueError:
            pass

    amt = int(code[i:j])
    i = j + 1

    for _ in range(amt):
        pos1_next = (pos1 + dir1) % grid.dimensions
        while grid[pos1_next] == " ":
            pos1_next = (pos1_next + dir1) % grid.dimensions
        if grid[pos1_next] == "#":
            break
        pos1 = pos1_next

    for _ in range(amt):
        pos2_next = pos2 + dir2
        dir2_next = dir2

        if pos2_next % grid.dimensions != pos2_next or grid[pos2_next] == " ":
            face_num = get_face_num(pos2)
            edge_pair = next(
                edge_pair for edge_pair in edge_pairs if (face_num, dir2) in edge_pair
            )
            face_num_next, edge_dir = next(
                (f, d) for (f, d) in edge_pair if f != face_num
            )
            offset = get_offset_amt(pos2, dir2)
            pos2_next = get_face_pos(face_num_next) + get_offset_vec(offset, edge_dir)
            dir2_next = -edge_dir

        if grid[pos2_next] == "#":
            break
        pos2 = pos2_next
        dir2 = dir2_next

    dir1 = dir1.rot(90 if code[j] == "L" else -90)
    dir2 = dir2.rot(90 if code[j] == "L" else -90)


def calc_password(pos: Vec2, dir: Vec2):
    return 1000 * (pos.x + 1) + 4 * (pos.y + 1) + [R, D, L, U].index(dir)


p1 = calc_password(pos1, dir1)
p2 = calc_password(pos2, dir2)
