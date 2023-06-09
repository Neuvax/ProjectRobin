<<<<<<< HEAD
"""@package docstring
Documentation for CPU module.
More details.
"""

import csv
import numpy

map_field = numpy.zeros(shape=(10,10))

def func():
    """Documentation for a function.
    More details.
    """
    pass
def do_instruction(inst):
    print(inst)
    print(map_field)

def read_file():
    inst_list = []
    with open('ProjectRobin\Deliverable 01\instructions.asm') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            inst_list.append(row)
    return inst_list
=======
import sys

robot_x = 0
robot_y = 0

direction = "->"
rotation_angle = 0

field = [["-" for _ in range(10)] for _ in range(10)]

def clear_field():
    global field
    field = [["-" for _ in range(10)] for _ in range(10)]

def plot():
    global field
    print("-------------------")
    field[robot_y][robot_x] = direction
    for row in field:
        print(" ".join(row))
    print()  # Salto de línea vertical

def turn(angle):
    global rotation_angle
    global direction
    rotation_angle = (rotation_angle - angle) % 360

    if rotation_angle == 0:
        direction = "->"
    elif rotation_angle == 90:
        direction = "↑"
    elif rotation_angle == 180:
        direction = "<-"
    elif rotation_angle == 270:
        direction = "↓"

def move(blocks):
    global robot_x
    global robot_y
    if direction == "->":
        if (robot_x + blocks) > 9:
            sys.exit("Invalid Operation, out of range")
        else:
            robot_x += blocks
    elif direction == "↑":
        if (robot_y - blocks) < 0:
            sys.exit("Invalid Operation, out of range")
        else:
            robot_y -= blocks
    elif direction == "<-":
        if (robot_x - blocks) < 0:
            sys.exit("Invalid Operation, out of range")
        else:
            robot_x -= blocks
    elif direction == "↓":
        if (robot_y + blocks) > 9:
            sys.exit("Invalid Operation, out of range")
        else:
            robot_y += blocks
    clear_field()
    plot()

def execute_actions_from_file(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            try:
                action, value = line.strip().split(',')
                if action == 'MOV':
                    move(int(value))
                elif action == 'TURN':
                    turn(int(value))
                else:
                    sys.exit("Invalid Operation, unrecognized")
            except ValueError:
                print("Invalid Operation, not enough values")
>>>>>>> f95a9776e4834b86838222453c2cccdb7d1e3b65

def main():
    plot()
    execute_actions_from_file('python/ProjectRobin/ProjectRobin/Deliverable 01/instructions.asm')

if __name__ == "__main__":
    main()
