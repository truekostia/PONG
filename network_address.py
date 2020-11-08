#find network address by bitwise operators
print(type(bin(192)))
print(bin(66))
#bin(192) & bin(255)

a = '{0:08b}'.format(192)
b = '{0:08b}'.format(168)
c = '{0:08b}'.format(0)
d = '{0:08b}'.format(66)

e = '{0:08b}'.format(255)
f = '{0:08b}'.format(255)
g = '{0:08b}'.format(255)
h = '{0:08b}'.format(0)

x = int(a + b + c + d)
y = int(e + f + g + h)
print(x)
print(y)

z = bin(0b11000000101010000000000000001010 & 0b11111111111111111111111100000000)
print(int(z[2:10], 2))
print(int(z[10:18], 2))
print(int(z[18:26], 2))
print(int(z[26:], 2))

ip1 = 192
ip2 = 168
ip3 = 0
ip4 = 66

m1 = 255
m2 = 255
m3 = 255
m4 = 0

print(ip1 & m1)
print(ip2 & m2)
print(ip3 & m3)
print(ip4 & m4)

print(ip1 or not (m1))
print(ip2 or not (m2))
print(ip3 or not (m3))
print(ip4 or not (m4))
