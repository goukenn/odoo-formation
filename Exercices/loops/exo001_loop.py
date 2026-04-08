for i in range(10):
    print(f"Bonjour {i}")

# exercise : 
# create a loop to go from 1 to 10. For each iteration check if the index is an even number.
# If its even, add it to a variable called total. Display the total at the end.
print('exerice 1:')
total = 0
for i in range(1, 11):
    if i % 2 == 0:
        total += i

print(f'total: {total}')

# exercise:
# Use a for loop to go. through a sentence. For Each character:
# - if it is vowel (a,i,o,e,u) print it in uppercase
# - if it a consonant (a letter but not a vowel), print it in lowercase.
# - if it is not a letter print "_" instead
# - 

sentence = "bonjour tout le monde 1454" # input('please enter a sentence: ')

for i in sentence:
    match(i):
        case i if i.lower() in 'aeiou'.split():
            print(i.upper(), end='')
        case i if i.isalnum():
            print(i.lower(), end='')
        case _:
            print('_', end="")

print('')
print ('4' in '158487')


# exercise: use of enumerate(...)
# use a loop to go through a list of fruits. For each elelement, display its index (starting from 1) and the element.
# 1: apple
# 2: banana
# 3: strawberry

for i, v in enumerate('apple,banana,strawberry'.split(','),20):
    print(f"{i} {v}")

# note start of enumerate is the start index of the enumerate - not the index in the list

# use of `next()`
