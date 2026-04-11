def location():
        x = 45
        print('sample')
print('running')

# depth is comming from long and must match 
def globalsaturation():
     def invocation():
        print('the invocation')
        return 'listing....'
     return 'globalsaturation' + invocation()


# depth can it contain class 
def container():
     def pow():
          return 'the pow'
     class sample:
          x = 4

          
          y = 8
     a = sample()
     print('call pow : ', pow())
     return a

class A:
     class B:
        pass
# if __name__ == '__main__':
# location()
print(globalsaturation()) 
print(container())

l = A.B

print(l, pow(88,2))
# print(container.sample)

