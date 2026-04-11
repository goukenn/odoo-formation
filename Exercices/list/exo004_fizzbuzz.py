# exercie:
# FizzBuzz
# Write a program that :
# - labels numbers divisible by 3 as "Fizz"
# - labels numbers divisible by 5 as "Buzz"
# - labels numbers divisible by 3 and 5 as "FizzBuzz"
# - display the current number if none of the conditions are true 


def fizzbuzz(n: int):
    """
    the **fizzbuzz** game\
    (int n)
    @param int n the maximum number  
    """
    for i in [ 'FizzBuzz' if (x % 3 == 0) and (x % 5 == 0) else 'Fizz' if x % 3 == 0 else 'Buzz' if x % 5 == 0 else x for x in range(1, n + 1)]:
        print(i, ' ', end="")

def fizzbuzzWithDic(n:int):
    dic = {
        3:"Fizz",
        5:"Buzz"
    }
    for x in range(1, i + 1):
        l = False
        msg = ''
        for y in dic.keys():
            if 0 == x % y:
                l = True
                msg = msg + dic[y]
        if not l:
            msg = str(x)
        print(msg, ' ', end="")

print('*' * 50)
print('FizzBuzz')
print('*' * 50)

# definition of tuples
c = 10
d = 20
# not unpack definition 
a,*p,_  = (c, d, 100,8, 80)
# a[0] = d
print(a,p, _)



try:
    i = int(input('please enter(number): '))
    fizzbuzz(i)
    print('')
except:
    print('not a valid number')


