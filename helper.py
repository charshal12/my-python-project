

def days_to_unit_params(num_of_days, conversion_unit):
    if conversion_unit == "hours":
        return f"{num_of_days} days are {num_of_days * 24}  hours"
    elif conversion_unit == "minutes":
        return f"{num_of_days} days are {num_of_days * 24 * 60}  minutes"
    elif conversion_unit == "seconds":
        return f"{num_of_days} days are {num_of_days * 24 * 60 * 60}  seconds"
    else:
        return "unsupported unit"


def validate_and_execute(days_and_unit_dictionary):
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

user_input_message = "Hey user, enter a number of days and conversion unit: \n"