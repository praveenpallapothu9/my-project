def num(number):
    if number > 17:
        numbers = number - 17
        numberss = numbers * 2
        print(f'the output that we got is :',numberss)
    elif number <= 17:
        numbers = number - 17
        numberss = abs(numbers)
        print(f'the output that we got is :',numberss)
    else:
        print("the output that we got is : 0")

num(22)
num(17)
num(14)
