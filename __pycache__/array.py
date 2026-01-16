import array as arr

var = arr.array("i",[1,3,5,3,7,9,3])
print("original array:"+str(var))


print("number of ourrences of 3:"+str(var.count(3)))

var.reverse()
print("reversed array:")
print(str(var))
