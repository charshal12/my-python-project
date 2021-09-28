print("201 is a great number")
print(3.4)
print(1)

# DataTypes
# TextType: Strings(str)=>"" OR ''
# Number Types:
# Integer(Int)[whole number, positive/negative, without decimals]
# Floating Point Number(Float)[number, positive/ negative, containing 1 or more decimals]#


# Arithmatic Operators
# How many minutes in 20 days which has 24 hrs and 60 mins.
print("*******Arithmatic Operations************")
print("20 days are " + str(50) + " minutes")
print(20 * 24 * 60)
print(f"20 days are {20 * 24 * 60} minutes")  # available in Python ver 3.6 {'f' stands for formatting}
print(f"35 days are {35 * 24 * 60 * 60} secs")  # 24 hrs and 60 mins and 60 secs
print(f"50 days are {50 * 24 * 60 * 60} secs")
print(f"100 days are {100 * 24 * 60 * 60} secs")

# To avoid repetitive changes in the statements, we use variables
print("***********With Variable*************")
calculation_to_seconds = 24 * 60 * 60
# Python is dynamically typed that means we just have to give variable and not the type along with it and assign values
# variable names should be descriptive 'calculation_to_seconds'
# we cannot use Reserved words as variables
print(f"35 days are {35 * calculation_to_seconds} secs")  # with variable

# Using more generic variables
print("***********With Generic Variable*************")
calculation_to_units = 24 * 60 * 60
name_of_units = "secs"
print(f"50 days are {50 * calculation_to_units} secs")
print(f"100 days are {100 * calculation_to_units} {name_of_units}")

calculation_to_unit = 24
name_of_unit = "Hours"
print(f"100 days are {100 * calculation_to_units} {name_of_unit}")

# To avaoid the duplication of logic in the code we use functions
print("*****************Functions***********************")


def days_to_units():  # functions OR Block
    print(f"120 days are {120 * calculation_to_units} {name_of_unit}")
    print("All good")


# Calling a function
days_to_units()  # unless we call a functions it is not going to execute.


# Passing Parameters in functions
def days_to_units_params(num_of_days):
    print(f"{num_of_days} days are {num_of_days * calculation_to_unit} {name_of_unit}")
    # print("All good")


# Cleaner code
days_to_units_params(35)
days_to_units_params(50)
days_to_units_params(100)
days_to_units_params(150)


# days_to_units_params() #Error for param is thrown


# Passing Custom message as Parameters in functions
def days_to_units_params_cust_msg(num_of_days, custom_message):
    print(f"{num_of_days} days are {num_of_days * calculation_to_unit} {name_of_unit}")
    print(custom_message)


days_to_units_params_cust_msg(20, "Awesome!")
days_to_units_params_cust_msg(75, "Looks Very Good!")


# we should not overload the function with 10 parameters

# Variable Scopes in Function
# A variable is only available from inside the region it is created
# Global Scope = Variables available from within any scope
# Local Scope = Variables created inside function

def scope_check(num_of_days):
    my_var = "variable inside function"  # variable inside function
    print(name_of_unit)  # Function body
    print(num_of_days)  # Function body
    print(my_var)


scope_check(89)

##User Inputs##
 
