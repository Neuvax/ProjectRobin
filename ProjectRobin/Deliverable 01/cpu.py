import csv

FIELD_SIZE = 10
map_field = [[0] * FIELD_SIZE for _ in range(FIELD_SIZE)]

def do_instruction(inst):
    print(inst)
    print(map_field)

def read_file():
    inst_list = []
    try:
        with open('instructions.txt') as txt_file:
            csv_reader = csv.reader(txt_file, delimiter=',')
            for row in csv_reader:
                inst_list.append(row)
    except FileNotFoundError:
        print("Error: File 'instructions.txt' not found.")
    return inst_list

def main():
    print("Hello World!")
    inst_list = read_file()
    for inst in inst_list:
        do_instruction(inst)

if __name__ == "__main__":
    main()
