l = [4, 5,1, 2, 9, 7, 10 ,8]
print("Original list:", l)


count = 0
for i in l:
    count += i

avg = count / len(l)

print(f" sum = {count}")
print(f" average is{avg}")

l.sort()

print("Smallest element is:", l[0])

print("Largest element is:", l[-1])
