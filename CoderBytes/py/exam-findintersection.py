def findintersection(str_arr: list) -> str:
    """Version avec list comprehension"""
    first, second = str_arr
    first = first.split(',')
    second = second.split(',')
    # first list compression 
    intersection = [k for k in second if k in first]
    
    return ','.join(intersection) if intersection else 'false'


# Test
print(findintersection(['1,2,3,4', '2,4,6,8']))  # 2,4
print(findintersection(['a,b,c', 'x,y,z']))      # false