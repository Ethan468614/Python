var = [1,2,3]

var2 = [4,5,6]

var3 = map(lambda x, y: x + y, var, var2)

print("addition of two lists:")
print(list(var3))

var4 = [1,2,3,4,5]

def sq(n):
    return n*n
var5 = list(map(sq, var4))
print("Squre of numbeers in the list:")
print(var5)