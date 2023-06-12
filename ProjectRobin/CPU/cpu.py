import sys
import subprocess

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

def compile_yacc(file):
    yacc_command = f"yacc -d {file}"
    subprocess.run(yacc_command, shell=True)

def compile_lex(file):
    lex_command = f"lex {file}"
    subprocess.run(lex_command, shell=True)

def compile_and_run(yacc_file, lex_file, input_file):
    compile_yacc(yacc_file)
    compile_lex(lex_file)
    subprocess.run("cc lex.yy.c y.tab.c -o ejecutable.exe", shell=True)
    subprocess.run(f"./ejecutable.exe {input_file}", shell=True)

def read_asm_file(file):
    with open(file, 'r') as asm_file:
        asm_code = asm_file.read()
    return asm_code

def main():
    yacc_file = "../Compiler/compiler.y"
    lex_file = "../Compiler/compiler.l"
    input_file = "../Compiler/input.txt"

    compile_and_run(yacc_file, lex_file, input_file)
    read_asm_file('instructions.asm')
    plot()
    execute_actions_from_file('instructions.asm')


if __name__ == "__main__":
    main()
