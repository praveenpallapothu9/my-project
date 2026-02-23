#greatest common divisor calculator

x , y = 12,18

if x > y:
    smaller = y
else:
    smaller = x
print(smaller)
for i in range(1,smaller):
    if x % i == 0  and y % i == 0:
        gcd  = i

print(gcd)
