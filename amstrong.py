a = int(input("Enter a 3-digit number:"))
c = a//100
d = a%100
e = d//10
f = d%10
g = c*c*c + e*e*e + f*f*f
print("Armstrong value is:",g)