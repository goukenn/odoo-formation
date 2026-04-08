# if condition:
#   ...
# elif condition:
#   ...
# else:


# match-case 
# match x:
#  case pattern:
#   ...
# case _:
#   ...

# documentation match case :

# create a nightclub bouncer program. Ask user for its age. if the user is less than 18 yerars oikd n access will be denied otherwise they are welcome.

v_age = (int(input('please enter your ages: ')))

if v_age < 18:
    print('sorry you are denied')
else:
    print('welcome')





# exercice 2 :
# create a script that asks the user for two numbers and then displays the larger one.
# Display "Tie" if ther is a tie.
# Bonus: Do it with three number 

number_1, number_2 = int(input('number 1: ')), int(input('number 2: '))

if number_1 == number_2:
    print('Tie')
elif number_2 > number_1:
    print (number_2)
else:
    print(number_1)

    