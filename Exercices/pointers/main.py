def update(*a):
    name, *_ = a # must a first element 
    print(a[0], name)
    a = 8

a = (12,65)

update(a)

print(a)