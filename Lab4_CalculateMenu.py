# Program name    : Functions.
# Program purpose : Modify the mortgage.py program function that will calculate mortgage payment.And also using keyword "import" to add in calculateMenu.py
# Created/revised : on 4/18/2020 jeff Kee 

"""
File: calculateMenu.py
Project 6.6

Provides a menu-driven tool for various calculation programs

 
"""

# import datetime library object

from datetime import datetime

# system related library
import os, os.path

import simpleInterest   ## import a local library function

import mortgage

#UPCASE variable names are global constant

QUIT = '99'  #All CAP is used for constant                           # if programmer seeing this all uppercase, 
COMMANDS = ('1', '2', '3','99') #using tuples for valid commend        # they know is a constant that define global need and shouldn't be changed

MENU = """
------------------------------
1    Calculate Simple Interest
2    Calculate Mortgage Payment
3    What is my current directory?
99   Quit the program
------------------------------
"""



"""
main: this is the main function will run your program.

It will print out the user selection menu, and then waiting for user's input,
and then execute based on user's input.

@param:  none
@return: non
"""

def sign():
    while True:
        print(MENU)
        command = acceptCommand()
        runCommand(command)
        if command == QUIT:
            print("Have a nice day!")
            break

"""
acceptCommand: this function will take user's input and will check for
valid input. If the input is valid, it will return user's input

@param:  none
@return: user's input
"""

def acceptCommand():
    """Inputs and returns a legitimate command number."""
    while True:
        command = input("Select one of the command number above: ")         # ！= is not equal to
        if command != '1' and command != '2' and command != '3' and \
           command != '99':
            print("Error: command not recognized")
        else:
            return command
        
        
"""
runCommand: this function will call different section of the program based on
which command you selected

@param:  command - which command or section of the code you want to run
@return: none
""" 
def runCommand(command):
    """Selects and runs a command."""
    if command == '1':
        print("\nCalculating Simple Interest\n")
        simpleInterest.simpleInterest()
    elif command == '2':
        print("\nCalculating mortgage payment\n")
        mortgage.mortgage()
    elif command == '3':
        printCurrentDirectory()
    elif command == '99':
        print("\nthank you\n")


    
"""
printCurrentDirectory:  this function will print out the current directory
you are in.

@param:  none
@return: none
"""
def printCurrentDirectory():
 #  print('\n')   # single quote is typically used for single character
    print('\n'"Current Directory:\n") # double quote for string, but can use either
    print(os.getcwd() + '\n') # print out the current directory
 #  print("\n") # no difference betwwen single or double quotes

"""
print_details: this function will print out the your name, current directory
you are in and the time you run this program.

You can use this function as 1st statement of your program so it will print
out the your name as part of the program.

@param:  name - this is the string you want the function to print
@return: none
"""    
def print_details(name):
    printCurrentDirectory()
    print(name)
    currentTime = datetime.now()
    print(currentTime)

 
"""
__main__: this is the main body of the program.  If this file is not imported
then the __name__ would be "__main__", so it will execute this section of
codes as the main program.

If this file is from import, then the __name__ would be "filename", then
this section of code if __name__ == "__main__"
will not run.

 
"""


if __name__ == "__main__":
 
    
    print_details("CNET-142: Kee Hock Meng, Lab4 Menu Function" + '\n') # this will print out at first 
    sign()
