# hostel-mess-management-system
a simple python project to manage hostel mess students records, meals and mess bills.

## About the Project

This is a simple Python project made to manage basic hostel mess records.

The program stores student details along with their mess type and the number of meals they have taken. It can also calculate the mess bill according to the number of meals.

The data is stored in a text file called `mess_records.txt.

## Features

The program has the following options:

1. Add Student
2. View Students
3. Mark Meal
4. Search Student
5. Calculate Mess Bill
6. Exit

### Add Student

The user enters the room number, student name and mess type (Veg/Non-Veg). The program also checks if the room number already exists.

### View Students

This option displays the details of all students, including their room number, name, mess type and meals taken.

### Mark Meal

The user enters a room number and one meal is added to that student's meal count.

### Search Student

A student can be searched using the room number. The program displays the student's details and number of meals taken.

### Calculate Mess Bill

The program calculates the mess bill based on the number of meals taken.

The cost of one meal is set to Rs. 60.

## Requirements

- Python 3.x
- No external libraries are required.

## How to Run

Open the project folder in a terminal and run:

`python hostel_mess.py`

If `python` does not work, try:

`python3 hostel_mess.py`

The main menu will then appear.

## Mess Bill Calculation

The bill is calculated using:

`Total Bill = Number of Meals Taken × Rs. 60`

For example, if a student takes 10 meals:

`10 × 60 = Rs. 600`

## Data Storage

The program uses `mess_records.txt` to store the student records.

The file contains:

`Room Number, Name, Mess Type, Meals Taken`

The file is created when a student is added to the system.

## Project Files

- `hostel_mess.py` - Main Python program
- `README.md` - Project information and instructions

## Conclusion

This project provides a simple way to maintain hostel mess records using Python and file handling. It keeps track of students, meals taken and the corresponding mess bill.
