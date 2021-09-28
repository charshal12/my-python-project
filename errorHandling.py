calculation_to_unit_1 = 24
name_of_unit_1 = "Hours"


def days_to_unit_params(num_of_days):
    return f"{num_of_days} days are {num_of_days * calculation_to_unit_1} {name_of_unit_1}"


def validate_and_execute():
    try:
        user_input_number = int(user_input)  # -10(int data type)
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
while user_input != "exit": # while condition and '!=', until user types 'exit' the program will run
    user_input = input("Hey user, enter a number of day and it will be converted to hours!\n")  # -10(string data type)
    validate_and_execute()

# When we have lot of conditions, insteadc of putting it into the if else or nested if else, we should use
# try-except
# You might forget to add in if else loop
