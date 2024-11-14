# Algorithm Document

------------------
* Purpose:  reads a file to a list
* Name: read_file_to_list
* Parameters:  filename (string, used to then read that file to a list)
* Return: name_list, (list, represents list of names from the file)
* Algorithm:
1. create empty list titled "name_list"
2. try
   1. open filename to read
   2. read each line of the file to name_list
   3. close filename
   4. return name_list
3. if that creates an error because the file is not found, except
   1. output to the user, "Error reading file"
   2. return name_list
--------------
* Purpose: main function
* Name: main
* Parameters: none
* Return: none
* Algorithm:
1. Output welcome message and purpose of the program to the user: ''Welcome! This program reads files of guest names and outputs seating.'
2. initialize count variable to 1
3. create empty list "name_list"
4. While count is less than 4
   1. variable file_name is set equal to user input with the message "Enter the file name of file {count}:"
   2. read_file_to_list is called with file_name as an argument, and its data is added to name_list
   3. count is incremented by 1
5. variable table is initialized to 1
6. variable seat is initialized to 1
7. for each name in name_list
   1. '~' is outputted 24 times
   2. output "Table {table}, Seat {seat}, {name}" 
   3. output '~' 24 times
   4. seat is incremented by 1
   5. If seat is greater than 5
      1. seat is set equal to 1
      2. table is incremented by 1
8. Output "{table} tables are needed."
-------------------------
1. call main function
