# datatype list [Strings, numbers, booleans]
# For Loop
# Basic List Operations
# Create  alist
# Access items of the list
# Add an item to the list
# Remove an item from list
# Change items in the list

[10, 15, 4, 9]
["Nina", "Ram", "Keya"]

calculation_to_unit_1 = 24
name_of_unit_1 = "Hours"


def days_to_unit_params(num_of_days):
    return f"{num_of_days} days are {num_of_days * calculation_to_unit_1} {name_of_unit_1}"


def validate_and_execute():
    try:
        user_input_number = int(num_of_days_element)  # -10(int data type)
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
    user_input = input("Hey user, enter a number of day as a comma separated value, it will be converted to hours!\n")  # -10(string data type)
    print(type(user_input.split(",")))
    print(user_input.split(","))
    for num_of_days_element in user_input.split(","):
        validate_and_execute()


# Create list
my_Months_List = ["Jan", "Feb", "Mar"]
my_Months_List[1] #Feb # to get a single value
print("Month with index 2: " + my_Months_List[2] + "\n")

# To get one element at a time use for loop
print("Printing list through FOR loop")
for num_of_month_element in my_Months_List:
    print(num_of_month_element)

# To append the element from list
my_Months_List.append("April")
print(my_Months_List)

