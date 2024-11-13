# Programmers:  Laure Patera and Rayan Haq
# Course:  CS151, Dr. Zee
# Due Date: 11/14/24
# Lab Assignment:  Lab 9
# Problem Statement:  Outputs seating cards for each guest at a dinner party and the number of tables needed
# Data In: file_name (which files to read to the list)
# Data Out:  Seating cards for each guest and number of tables needed
# Credits: Codes used in class from the repository
# Input Files: must be .txt, isaacman.txt, yalew.txt, and nweke.txt expected


# Purpose:  reads file to a list
# Parameters: filename (string, used to then read that file to a list)
# Return: name_list, list, represents list of names from the file
def read_file_to_list(filename):

    #Initialize list
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

# Purpose:  main function
# Parameters: none
# Return: none
def main ():
    #Output welcome message and purpose of program
    print('Welcome! This program reads files of guest names and outputs seating.')

    #Initialize count and list
    count = 1
    name_list = []

    #Asks user to enter a filename three times and calls read_file_to_list, adding the names of each file to list name_list
    while count < 4:
        file_name = input(f'Enter the name of file {count}:')
        name_list += read_file_to_list(file_name)
        count += 1

    #Initialize variable table and seat
    table = 1
    seat = 1

    #For each name in name_list, print the seating card
    for name in name_list:
        print('~' * 24)
        print(f'Table {table}, Seat {seat}, {name}', end = '')
        print('~' * 24)

        #Increment seat and table, so that each guest has a different seating assignment in order
        seat += 1
        if seat > 5:
            seat = 1
            table += 1

    #Output how many tables are needed
    print(f'{table} tables are needed.')

#call main function
main()


