#x, y, z = 1,2,3
#x,y,z=3,3,3

def sum(x,y,z):
    sum = 0
    if x == y ==z:
        a = (x + y + z) * 3
        sum = sum + a
        print(sum)
    else:           
        sum = sum + x + y + z
        print(sum)
sum(1,2,3)
sum(3,3,3)