import csv

FIELD_SIZE = 10
map_field = [[0] * FIELD_SIZE for _ in range(FIELD_SIZE)]
current_position = [0, 0]

def do_instruction(inst):
    global map_field, current_position

    if inst[0] == 'mov':
        steps = int(inst[1])
        move_robot(steps)
    elif inst[0] == 'turn':
        angle = int(inst[1])
        turn_robot(angle)
    elif inst[0] == 'draw':
        draw_field()
    else:
        print("Unknown instruction:", inst)

def move_robot(steps):
    global map_field, current_position

    x, y = current_position
    if map_field[x][y] == 1:
        print("Invalid move. Obstacle at current position.")
        return

    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Right, Down, Left, Up
    for _ in range(steps):
        dx, dy = directions[0]
        new_x = x + dx
        new_y = y + dy

        if 0 <= new_x < FIELD_SIZE and 0 <= new_y < FIELD_SIZE:
            x = new_x
            y = new_y
            current_position = [x, y]
            map_field[x][y] = 1
        else:
            print("Invalid move. Out of bounds.")
            return

def turn_robot(angle):
    global map_field

    if angle == 90:
        map_field = list(zip(*reversed(map_field)))
    elif angle == 180:
        map_field = [list(reversed(row)) for row in reversed(map_field)]
    else:
        print("Invalid turn angle.")

def draw_field():
    for row in map_field:
        print(row)

def read_file():
    inst_list = []
    try:
        with open('./instructions.asm') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            for row in csv_reader:
                inst_list.append(row)
    except FileNotFoundError:
        print("Error: File 'instructions.asm' not found.")
    return inst_list

def main():
    print("Hello World!")
    inst_list = read_file()
    for inst in inst_list:
        do_instruction(inst)

if __name__ == "__main__":
    main()
