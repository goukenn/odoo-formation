# exercices:
# Ask the user for 10 numbers and put htem in a list. Find the maximum in a list and sum all the elements of the list.

# sentence = map(int, input('give a list of number (comma separated): ').split(','))
# m, total = 0, 0
# for x in sentence:
#     m = max(m, x); total = total + x
# print(f"max: {m} total: {total}")

# not ";" is used to separate multiple instruction on a single line

# use of list comprehension 

def maxAndTotal(sentence):
    m, total = 0, 0
    for x in sentence:
        m = max(m, x); total = total + x
    return m, total
sentence = [int(input(f'please enter {x + 1}: ')) for x in range(4)]

print(maxAndTotal(sentence))