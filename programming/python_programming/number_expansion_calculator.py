numbers = int(input("enter the number:"))
print(f"the given number is :",numbers)
sum =0
while numbers > 0:
    sum =  sum+numbers
    digits = numbers % 10
    numbers = numbers // 10
print(f"the output that we got is :",sum)