# SET ==> Datatype with UNIQUE values ==> Avoid duplication
# {10, 30, 45}
# In LIST we can send duplicate values but not in SET

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
    list_of_days = user_input.split(",")

    print(list_of_days)
    print(set(list_of_days))

    print(type(list_of_days))
    print(type(set(list_of_days)))

    for num_of_days_element in set(list_of_days):
        validate_and_execute()
"""OUTPUT:
Hey user, enter a number of day as a comma separated value, it will be converted to hours!
10 , 23, 56, 44, 23
['10 ', ' 23', ' 56', ' 44', ' 23']
{' 56', '10 ', ' 44', ' 23'}
<class 'list'>
<class 'set'>
56 days are 1344 Hours
10 days are 240 Hours
44 days are 1056 Hours
23 days are 552 Hours"""

my_week_set = {"Monday", "Tuesday", "Wednesday"}
# Items in the set do not have a DEFINED ORDER!
# Items cannot be referred to by index!
# items cannot be changed, only added/ removed!

# We can only access them in loop for operations
print("Looping the SET: ")
for element in my_week_set:
    print(element)

# Add elements to set
print("Adding an element in the SET: ")
my_week_set.add("Thursday")
print(my_week_set)

#Remove Element
print("Removing an element in the SET: ")
my_week_set.remove("Monday")
print(my_week_set)