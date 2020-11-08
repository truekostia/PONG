#count number of networks in class B IP address
x = 128
y = -1
n = []
m = []
n.append(x)
while x < 191:
    x += 1
    n.append(x)
#print(n)
for i in n:
    if y == 255:
        y = -1
    while y < 255:
        y += 1
        m.append([i, y])
#print(m)
print(len(m))

