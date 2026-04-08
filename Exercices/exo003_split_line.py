# Write a Python script that takes a string text and an integer max_length.
# if the length is greater than max_length , truncate it to the first max_length characters and add "..."
# at the end. Otherwise, keep the string unchanged.

max_length = int(input('please max line length: '))
word = input('the phrase: ')
if len(word) > max_length:
    word = word[:max_length] + '...'

print('the word ', word, end='\n!!!')