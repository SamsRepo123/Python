import calendar
import random
from datetime import date
from datetime import datetime

#I took single digit numbers from 0 to 9
li = [1,2,3,4,5,6,7,8,9,0]

#i am shuffling it two times to get good random numbers
random.shuffle(li)
random.shuffle(li)

#I am using date function to know when i last time generated the number
today = date.today()
now = datetime.now()

def findDay(date): 
    born = datetime.datetime.strptime(date, '%d %m %Y').weekday() 
    return (calendar.day_name[born]) 
  
# Driver program

print ("\nYour new code is: ", end="",file=open("output.txt", "a"))
for i in range(0, 6): 
    print (li[i], end=" ",file=open("output.txt", "a")) 
print("\r",file=open("output.txt", "a"))

d1 = today.strftime("%d-%m-%Y")
current_time = now.strftime("%H:%M:%S")
# Saving the new genrated code with timestamp in text file called output.txt
print("Generated Time =", current_time, file=open("output.txt", "a"))
print("Generated date:", d1, file=open("output.txt", "a"))
date = d1

