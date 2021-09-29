# Dictionary datatype
# in this we have key-value pair
# representation:  {"days": 20, "unit": "hours"}


calculation_to_unit_1 = 24
name_of_unit_1 = "Hours"


def days_to_unit_params(num_of_days):
    return f"{num_of_days} days are {num_of_days * calculation_to_unit_1} {name_of_unit_1}"


def validate_and_execute():
    try:
        user_input_number = int()  # -10(int data type)
        if user_input_number > 0:
            calculated_value = days_to_unit_params(user_input_number)  # passes value into function
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

    # print(list_of_days)
    # print(set(list_of_days))
    #
    # print(type(list_of_days))
    # print(type(set(list_of_days)))
    #
    # for num_of_days_element in set(list_of_days):
    # validate_and_execute()
