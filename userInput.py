# Passing Parameters in functions
calculation_to_unit = 24
name_of_unit = "Hours"


def days_to_unit_params(num_of_days):
    return f"{num_of_days} days are {num_of_days * calculation_to_unit} {name_of_unit}"


# num_of_days: is interpreted  as a String, then it gives wiered output
# assigning variable to a variable
# my_var = days_to_unit_params(85)
# print(my_var)

user_input = input("Hey user, enter a number of day and it will be converted to hours!\n")
user_input_number = int(user_input)
days_to_unit_params(user_input_number)
calculated_value = days_to_unit_params(user_input_number)
print(calculated_value)
