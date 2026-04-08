# exercies:
# create a game where the computrer chooses a random number between 1 and 100. The user has a limited number of attempts
# for example, 10) to guess the number. With each attempt, the program indicates whether the number is higher or lower than the user's guess.


from random import randint


x = randint(1,100)
i = 0

while i < 10:
    i = i + 1
    y = int(input("give a number: "))
    if y == x:
        print('success')
        break
    elif y < x:
        print('* lower number')
    else:
        print('* bigger number')

