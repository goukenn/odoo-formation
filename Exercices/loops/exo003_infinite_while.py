# exercise: infinite while with break
# use a loop to ask the user to provide a color, display their response, and ask if they want to continue providing a color or stop.

while True:
    color = input('give a color? ')
    if input('do you want to exit ? (y/N)')=='y':
        break

# for i in range(100):
#     if i >25:
#         break
#     print('value: ', i)


# exercise:
# Use a for loop to go through each character in a text. If the character is not a letter skip, if the character is a letter, print it in uppercase
# 
sentence = 'Bonjour tout le monde'

for i in sentence:
    if not i.isalpha():
        continue
    print(i.upper(), end='')

print('')