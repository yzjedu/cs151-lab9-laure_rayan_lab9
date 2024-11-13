def read_file_to_list(filename):
    data = []
    try:
        # Open the file for reading
        file_data = open(filename, "r")

        # Read all lines from the file into a list
        name_list = file_data.readlines()

        # Close the file after reading
        file_data.close()

        # Return the list of data
        return name_list
    except FileNotFoundError:
        # Print an error message and return an empty list
        print("Error reading file")
        return data

def main ():
    print('Welcome! This program reads files of guest names and outputs seating.')
    count = 1
    name_list = []
    while count < 4:
        file_name = input(f'Enter the name of file {count}:')
        name_list += read_file_to_list(file_name)
        count += 1
    table = 1
    seat = 1
    for name in name_list:
        print('~' * 24)
        print(f'Table {table}, Seat {seat}, {name}', end = '')
        print('~' * 24)
        seat += 1
        if seat > 5:
            seat = 1
            table += 1
    print(f'{table} tables are needed.')

main()


