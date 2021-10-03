#Logically organize your Python code
#How to connect multiple files in python, we connect them through "modules"
# we will call here helper.py
# Anything (functions, variables in a .py file (module) are the definations)
import helper
#from helper import validate_and_execute, user_input_message
# from helper import *
# you can add different name to the file ==> "import helper as h" and athen replace helper with h



user_input = ""
while user_input != "exit":  # while condition and '!=', until user types 'exit' the program will run
    user_input = input(helper.user_input_message)  # -10(string data type)
    days_and_unit = user_input.split(":")
    days_and_unit_dictionary = {"days": days_and_unit[0], "unit": days_and_unit[1]}
    helper.validate_and_execute(days_and_unit_dictionary)
    #validate_and_execute(days_and_unit_dictionary)