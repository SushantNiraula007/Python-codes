def myfunction():
    a = 10
    b = 20
    print("Variable a:", a)
    print("Variable b:", b)
    return a+b
print (myfunction())

c = myfunction().a
d = myfunction().b

print("Variable c:", c)
print("Variable d:", d)