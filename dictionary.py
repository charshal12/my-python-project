# Dictionary datatype
# in this we have key-value pair
# representation:  {"days": 20, "unit": "hours"}


def days_to_unit_params(num_of_days, conversion_unit):
    if conversion_unit == "hours":
        return f"{num_of_days} days are {num_of_days * 24}  hours"
    elif conversion_unit == "minutes":
        return f"{num_of_days} days are {num_of_days * 24 * 60}  minutes"
    elif conversion_unit == "seconds":
        return f"{num_of_days} days are {num_of_days * 24 * 60 * 60}  seconds"
    else:
        return "unsupported unit"


def validate_and_execute():
    try:
        user_input_number = int(days_and_unit_dictionary["days"])  # -10(int data type)
        if user_input_number > 0:
            calculated_value = days_to_unit_params(user_input_number,
                                                   days_and_unit_dictionary["unit"])  # passes value into function
            print(calculated_value)
        elif user_input_number == 0:
            print("You entered ZERO, please enter positive number!")
        else:
            print("You entered a negative number, no conversion for you!")
    except ValueError:
        print("Your number is not an input, Dont ruin my program!")
    # except:
    #     print("Your number is not a valid number, Dont ruin my program!")


user_input = ""
while user_input != "exit":  # while condition and '!=', until user types 'exit' the program will run
    user_input = input("Hey user, enter a number of days and conversion unit: \n")  # -10(string data type)
    days_and_unit = user_input.split(":")
    print(days_and_unit)
    days_and_unit_dictionary = {"days": days_and_unit[0], "unit": days_and_unit[1]}
    print(days_and_unit_dictionary)
    print(type(days_and_unit_dictionary))
    validate_and_execute()

''' How do we access elements from dictionary and list.
my_List = ["20","30","67"]
print(my_List[2])

my_dictionary = {"days": 20, "unit": "hours", "message": "All good!"}
print(my_dictionary["message"])'''

'''''#Revision of datatypes
message = "enter some value" # String
days = 23   # IInteger
price = 98.55 # Float
valid_number = True    # boolean
exit_input = False # boolean
list_of_dayss = [23, 45, 65, 28] # List
list_of_month = ["January",  "February", "March", "April"] # List
set_of_days = {25, 45, 78}
my_dictionary = {"days": 20, "unit": "hours", "message": "All good!"} # dictionary
Depending on what you try to achieve in your program, you need a different data type to achieve exactly that'''
