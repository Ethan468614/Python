
def mult(tup):
    product = 1
    for num in tup:
        product *= num
    return product

tuple1 = (24, 12, -5, 8, 9)

tuple2 = (1, 5, 38, 23, 7)

print("The product of tuple1 is:", mult(tuple1))
print("The product of tuple2 is:", mult(tuple2))
