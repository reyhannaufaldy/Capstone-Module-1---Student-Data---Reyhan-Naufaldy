Student Data Management System
Brief Description: The Student Data Management System is a console-based application designed to manage student data. This application provides CRUD (Create, Read, Update, Delete) functionalities to facilitate adding, displaying, updating, and deleting student records. The program uses efficient data structures to store information and ensures data integrity through rigorous input validation.

Key Features:

Create: Adds new student records to the system. Users can input information such as Student ID (SID), name, status, gender, and scores in Singing, Rapping, and Dancing. The system validates the input to ensure that the data entered is accurate and complete.
Read: Displays student data. Users can view a complete list of students or search for a student by SID. The data displayed includes SID, name, status, gender, and relevant scores.
Update: Updates existing student information. Users can select which field to update, such as name, status, gender, or scores, and the system will validate the input before making changes.
Delete: Removes student records from the system. Users can delete records based on SID, and the system will prompt for confirmation before permanently deleting the data.
Data Structure:

List of Dictionaries: Student data is stored in a list containing dictionaries. Each dictionary represents a single student and holds attributes such as SID, name, status, gender, and scores.
Why Used: This structure simplifies searching, updating, and deleting student data. The list allows iteration through all entries, while dictionaries provide quick access to student attributes using key-value pairs.
Control Structures:

while Loop: Used for input validation, ensuring that data entered meets the desired format (e.g., SID must be 7 digits).
if, elif, else: Used to direct program flow based on user choices. This structure allows handling different options in an organized manner.
for Loop: Used to iterate through student data, making it easier to display and process each entry in the list.
Global Functions:

Global Functions: Functions such as input_sid() and main_menu() are used globally across the program to handle common operations and menu navigation.
Why Used: They simplify access to frequently used functions and help keep the code modular and organized.
Running the Program:

Execute the Python file to start the application.
Select options from the main menu to access CRUD features.
Follow on-screen prompts to add, display, update, or delete student data.
Installation and Prerequisites:

Python 3.x
No additional libraries required
