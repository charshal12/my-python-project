# 1) Accept user input of goal and a deadline
# 2) Print back:
        # How much time remains until that deadline?
# We make use of determine module for the time calculation

#Solution

from datetime import datetime

user_input = input("Enter your goal with a deadline and separate it with colon \n")
input_list=user_input.split (":")
goal = input_list[0]
deadLine = input_list[1]
print(input_list)

deaLine_date = datetime.datetime.strptime(deadLine, "%d.%m.%Y")
# calculate how many days from now till deadLine

print(datetime.datetime.today())
today_date=datetime.datetime.today()

time_till =  deaLine_date - today_date
hours_till = int(time_till.total_seconds() / 60 / 60)
print( f"User time remaining for your goal : {goal} is { time_till.days} days")
print( f"User time remaining for your goal : {goal} is {hours_till} hours")


