# WRITE YOUR CODE SOLUTION HERE
from datetime import date
date = date.today()

print(date )

date_ =str(input('Enter the date(for example:09 02 2019):'))
day_name= ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat','Sun']
day = datetime.datetime.strptime(date, '%d %m %Y').weekday()
print(day_name[day]) 

if day_name [0,1,2,3,4,5]:
    fare = '100'
    elif day_name [6] :
        fare = '60'
        else:
            fare = '80'
print(fare)
