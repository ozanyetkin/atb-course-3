

a = ["a", "b"]
b = ["a", "b"]

print(id(a) == id(b))

a = ["adsvcgfhx", "b", 3]
b = a

print(id(a) == id(b))

a.append("c")

print(b)

x = 10
y = 10

print(id(x) == id(y))
x=y
y+=1
print(id(x)==id(y))


