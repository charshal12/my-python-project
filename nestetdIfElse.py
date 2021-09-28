calculation_to_unit_1 = 24
name_of_unit_1 = "Hours"


def days_to_unit_params(num_of_days):
    return f"{num_of_days} days are {num_of_days * calculation_to_unit_1} {name_of_unit_1}"


def validate_and_execute():
    if user_input.isdigit():
        user_input_number = int(user_input)  # -10(int data type)
        if user_input_number > 0:
            calculated_value = days_to_unit_params(user_input_number)  # passes value into function
            print(calculated_value)
        elif user_input_number == 0:
            print("You entered ZERO, please enter positive number!")
    else:
        print("Your number is not an input, Dont ruin my program!")


user_input = input("Hey user, enter a number of day and it will be converted to hours!\n")  # -10(string data type)
validate_and_execute()
