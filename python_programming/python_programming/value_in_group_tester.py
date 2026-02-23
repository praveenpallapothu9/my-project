lists = [1,5,8,3]

def value_in(lists,value):
    if value in lists:
        print(True)
    else:
        print(False)

value_in(lists,3)
value_in(lists,-1)
value_in(lists,1)
