#Late Grade Calculator
#Written by: Tyler Kness-Miller
#24 September 2019
#This script takes in 3 dates: Date Turned In, Due Date, and Semester End.
#Using these dates, it calculates the slope to find the rate at which percentage
#points decrease as each hour goes by. 
# It outputs the equation it calculates, as well as the amount of percentage points that is possible.

import datetime

#Output directions.
print("For the purposes of this program, all dates must be inputted in the following format:")
print("MM-DD-YYYY HH:MM")
print("Time must be inputted in military format.\n")

#Take in user input and convert into dates using given format.
print("First, input the date the assignment was due:")
dueDate = datetime.datetime.strptime(input(), '%m-%d-%Y %H:%M')

print("Next, input the date submissions are allowed until:")
semEnd = datetime.datetime.strptime(input(), '%m-%d-%Y %H:%M')

print("Finally, input the date that the assignment was turned in:")
turnedIn = datetime.datetime.strptime(input(), '%m-%d-%Y %H:%M')

#Calculate slope using changeY/ChangeX, where Y is in %.
dateDif = semEnd - dueDate
dateDifHrs = dateDif.total_seconds() / 3600
slope = (100 / dateDifHrs) * -1

#Print equation used to calculate possible percentage.
print("Your equation: y = (" + str(slope) + ")x + 100\n")

#Output results. 
assignmentDif = ((turnedIn - dueDate).total_seconds() / 3600) * slope + 100

print("Percentage Possible: " + str(assignmentDif) + "%\n")