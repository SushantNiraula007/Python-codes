a = [1, 2, 3, 4, 5]
b = [1, 2, 3, 4, 5]
c = a

x = "Sushant"
y = "Sushant"
z = x

print("When compared with array:")
print(a is c)
print(a is b)

print("id(a) : ", id(a))
print("id(b) : ", id(b))
print("id(c) : ", id(c))

print("When compared with string:")
print(x is z)
print(x is y)

print("id(x) : ", id(x))
print("id(y) : ", id(y))
print("id(z) : ", id(z))