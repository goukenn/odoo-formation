# # Set exercises
# ## 1. Find common elements
# Write a function common_elements(list1, list2) that takes two lists as input
# and returns a list containing only the elements present in both lists, without duplicates.
# output : common_elements([1, 2, 3, 4], [3, 4, 5, 6]) => [3, 4]

def common_elements(ls1, ls2):
    return list(set(ls1) & set(ls2)) # intersection 

print('common elements => ', common_elements([1, 2, 3, 4], [3, 4, 5, 6]))

# ## 2. Remove duplicates
# Write a function remove_duplicates(lst) that takes a list as input
# and returns a new list containing the same elements, but without duplicates.
# output : remove_duplicates([1, 2, 2, 3, 4, 4, 5]) => [1, 2, 3, 4, 5]
def remove_duplicates(ls1):
    # difference and union
    return list(set(ls1))  # convert list => set =>  

print('remove_duplicates => ', remove_duplicates([1, 2, 2, 3, 4, 4, 5]))


# ## 3. Find unique elements
# Write a function unique_elements(list1, list2) that takes two lists as input
# and returns a list containing the elements that appear in only one of the two lists,
# without duplicates.
# output : unique_elements([1, 2, 3], [2, 3, 4]) => [1, 4]

def unique_elements(ls1, ls2):
    # difference and union
    ls1 = set(ls1)
    ls2 = set(ls2)
    return list((ls2 - ls1) | (ls1 - ls2))

print('unique_elements => ', unique_elements({1,2,3},{2,3,4}))

# ## 4. Check for common elements
# Write a function has_common_elements(list1, list2) that takes two lists as input
# and returns True if they have at least one element in common, otherwise False.
# outputs :
# - has_common_elements([1, 2, 3], [4, 5, 6]) => False
# - has_common_elements([1, 2, 3], [3, 4, 5]) => True
def has_common_element(list1, list2):
    return len(list1 & list2) > 0


# ## 5. Count unique elements
# Write a function count_unique_elements(lst) that takes a list as input
# and returns the number of unique elements it contains.
# output : count_unique_elements([1, 2, 2, 3, 3, 3, 4]) => 4

def count_unique_elements(list):
    return { i for i in list}.__len__()


print('has common  => ', has_common_element({1,2,3}, {4,5,6}))
print('has common  => ', has_common_element({1,2,3}, {3, 4,5,6}))
print('count_unique_elements => ', count_unique_elements([1,2,2,3,3,3,4]))