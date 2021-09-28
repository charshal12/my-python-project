# We use conditions for below few reasons
# 1. Its should make sense(-negative output)
# 2.The program should not get crashed
# Conditionals
# Equals: a == b
# Not Equals: a != b
# Less Than : a < b
# Less Than or Equal To : a <= b
# Greater Than: a > b
# Greater Than or equal to : a >= b
# By validating user input validation


calculation_to_unit_1 = 24
name_of_unit_1 = "Hours"


def days_to_unit_params(num_of_days):
    condition_check = num_of_days > 0
    print(type(condition_check))
    if num_of_days > 0:  # evaluates condition in 'if'
        return f"{num_of_days} days are {num_of_days * calculation_to_unit_1} {name_of_unit_1}"  # if positive , return this
    elif num_of_days == 0:
        return "You entered ZERO, please enter positive number!"


def validate_and_execute():
    if user_input.isdigit():
        user_input_number = int(user_input)  # -10(int data type)
        calculated_value = days_to_unit_params(user_input_number)  # passes value into function
        print(calculated_value)
    else:
        print("Your number is not an input, Dont ruin my program!")



user_input = input("Hey user, enter a number of day and it will be converted to hours!\n")  # -10(string data type)
validate_and_execute()

# check the data type
print(type(30.23))
print(type(9))
print(type("Hello!"))
