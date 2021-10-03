'''import helper'''
import os
import logging

print(os.name)

logger = logging.getLogger("Main")
logger.error("Error happened in app!")

'''user_input = ""
while user_input != "exit":  # while condition and '!=', until user types 'exit' the program will run
    user_input = input(helper.user_input_message)  # -10(string data type)
    days_and_unit = user_input.split(":")
    days_and_unit_dictionary = {"days": days_and_unit[0], "unit": days_and_unit[1]}
    helper.validate_and_execute(days_and_unit_dictionary)
    #validate_and_execute(days_and_unit_dictionary)'''