def fizzbuzz(n: int):
    """
    the **fizzbuzz** game\
    (int n)
    @param int n the maximum number  
    """
    l = []
    for i in [ 'FizzBuzz' if (x % 3 == 0) and (x % 5 == 0) else 'Fizz' if x % 3 == 0 else 'Buzz' if x % 5 == 0 else x for x in range(1, n + 1)]:
        l.append(str(i))
    
    return ' '.join(l)

print(fizzbuzz(16))
