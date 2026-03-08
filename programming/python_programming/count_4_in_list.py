def count(list_count):
    count = 0
    for i in list_count:
        if i == 4:
            count = count+1
    print(count)

list_count = [1,4,6,7,4]
count(list_count)
list_count = [1,4,6,7,4,4,4]
count(list_count)