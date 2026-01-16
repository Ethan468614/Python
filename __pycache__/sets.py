var = {1, 2,3}
print(var)

var = {1.0, "Hello", (1,2,3)}
print(var)

var = {1,2,3,2,4,4,5}
print(var)

var = set([1,2,3,2])
print(var ,"\n")

var2  = set([0,1,3,4,5])
print("original set:")
print(var2)
var2.pop()
print("set after pop:")
print(var2)