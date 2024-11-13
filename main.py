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
    except:
        # Ensure the file is closed in case of an error
        file_data.close()

        # Print an error message and return an empty list
        print("Error reading file")
        return data

def main ():
    count = 0
    while count < 3:
        file_name = input("Enter the name of the file to read: ")
        name_list = read_file_to_list(file_name)
        count += 1
    table = 1
    seat = 1
    for name in name_list:
        print('~' * 24)
        print(f'Table {table}, Seat {seat}, {name}')
        print('~' * 24)
        seat += 1
        if seat > 5:
            seat = 1
            table += 1
    print(f'{table} tables are needed.')


