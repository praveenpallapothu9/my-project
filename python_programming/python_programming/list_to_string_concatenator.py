lists = [1,5,12,2]
def list_to_string(lists):
    output = ''
    for i in lists:
        print(i)
        print(type(i))
        output += str(i)
    print(output)
    print(type(output))

list_to_string(lists)


