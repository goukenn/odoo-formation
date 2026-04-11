# ## Dictionary from two lists

# Create a dictionary from 2 lists (["A","B","C"] and ["1","2","3"] using dictionary comprehension and the zip() function.

l1 = ["A","B","C"]
l2 = ["1","2","3"]
print('with zip function')
d = dict(zip(l1, l2))
print(d) # zip(l1, l2))

# with comprehensive expression

print('with comprehension')
m = {l1[i]:l2[i] for i in range(len(l1))}
print(m)