# Write a script that takes a sentence stored in a variable text.
# - Split the sentence into a list of words using the appropriate string method
# - Then, join the words back together into a nex string where each word is separated by a hyphen "-"

v_i = input('please enter a sentence: ')

tab = v_i.strip().split(' ')
print("-".join(tab))


# with regex
