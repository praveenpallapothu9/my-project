'''def string_prefix_copies(x,y,z):    
    names = x
    values = y
    sorts = z
    sub_string = names[:values]
    print(sub_string)
    string_copy = sub_string * sorts
    print(string_copy)
string_prefix_copies("abcdef",3,2)
string_prefix_copies("p",2,3)
'''

#names = input("enter the string:")
#sorts = int(input("enter the number of copies:"))
def strings(names , sorts):
        #hello 3 hehehe
    flen = 2
    sub_string = names[:flen]
    string_copy = sub_string*sorts
    print(string_copy)

#strings(names,sorts)
strings('abcdef',3)
strings('p',4)
