def new_string(string):
    if string.startswith('Is'):
        print(string)
    else:
        print("Is"+string)
        return "Is"+string

stri = input("enter the string:")
print(stri)
new_string(stri)
print(new_string(stri))