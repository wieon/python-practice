# switch variables

# method 1
a = 2
b = 3
print("a=", a)
print("b=", b)
temp = a
a = b
b = temp
print("a=", a)
print("b=", b)

# method 2
a, b = b, a
# python特有的方式
