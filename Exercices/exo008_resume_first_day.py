# exercice:
# create a program that asks the user for two numbers 
# if one is positive and the other negative, the the program displays "Congratulations!"


v_x, v_y = float(input('enter a number 1: ')), float(input('enter number 2: '))
if v_x >= 0 and v_y<0:
    print('Congradulations!')

# Exercise
# create a program that tells the user whether it is cold or not.
# ast the user for temperature
# if the temp is less than 10°, then it is cold.
# if the temp is between 10° and 15°, then it is cold.
# if the temp is between 15° and 20°, then it is warm.
# if the temp is above 20°, then it is warm.


temp = float(input('selected temp(°): '))

# if temp <= 10:
#     print('it is very cold')
# elif 10 < temp <= 15:
#     print('it is cold')
# elif 15 < temp <= 20:
#     print('it is warm')
# else:
#     print('it is very warm')


match temp:
    case temp if temp <= 10 :
        print('it is very cold')
    case temp if 10 < temp <= 15:
        print('it is cold')
    case temp if 15 < temp <= 20:
        print('it is normal')
    case temp if temp > 20:
        print('it is hot')