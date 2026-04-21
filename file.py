a = "Okay"
f = open("file.txt", "a")
data = f.write(a)
print(data)
f.close()

b = "Nice"
g = open("file.txt", "w")
data1 = g.write(b)
print(data1)
g.close()

c = "Include this"
h = open("file.txt", "r")
data2 = h.read(c)
print(data2)
f.close()