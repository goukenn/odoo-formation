# Write a function that calculate the perimeter of a circle using pi from the math library
# Tips: perimeter = 2 * PI * Radius

import math 
import datetime
def circle():
    radius = int(input('enter a radius: '));
    if radius>0:
        print('the perimeter: ', round(math.pi * 3 * radius, 2))


# define sample : create a function that returns today's date + one week
def showDate():
    return datetime.date.today().__add__(datetime.timedelta(weeks=1))

# print(showDate())


# Exercise:
# Create a program that asks the user for an offset (in hours) from UTC (GTM+0) and return the current date and time corresponding time zone

# | Code | Meaning    | Example |
# | ---- | ---------- | ------- |
# | `%Y` | Year (2026) | 14      |
# | `%y` | Year (26) | 14      |
# | `%m` | mounth (04) | 14      |
# | `%d` | days(04) | 14      |
# | `%H` | Hour (24h) | 14      |
# | `%I` | Hour (12h) | 02      |
# | `%M` | Minutes    | 05      |
# | `%S` | Seconds    | 09      |
# | `%p` | AM/PM      | PM      |

def showDateTime():
    offset = int(input('enter offset '))
    return datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=offset)))


print(showDateTime().__format__('%Y-%m-%d %H:%M:%S'))