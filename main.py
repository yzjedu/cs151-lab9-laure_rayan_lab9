def read_file_to_list(filename):
    data = []
    try:
        # Open the file for reading
        file_data = open(filename, "r")

        # Read all lines from the file into a list
        data = file_data.readlines()

        # Close the file after reading
        file_data.close()

        # Return the list of data
        return data
    except:
        # Ensure the file is closed in case of an error
        file_data.close()

        # Print an error message and return an empty list
        print("Error reading file")
        return data

def main ():
    file_name=input("Enter the name of the file to read: ")
    list = read_file_to_list(file_name)
    tables =1
    seat = 1
    for name in list:
        print()


