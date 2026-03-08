def number(n):
    return ((abs(1000-n) <= 100) or (abs(2000-n)<=100))

print(number(1000))
print(number(900))
print(number(800))
print(number(700))