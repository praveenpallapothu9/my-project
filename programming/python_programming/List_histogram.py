# def items(lists):
#     for i in lists:
#         print(i*'*')
def items(lists):
    for i in lists:
        #print(i)
        output = ""
        n = i
        while n>0:
            output += "*"
            n=n-1
        print(i,output)



lists = [2,3,6,5]
items(lists)
