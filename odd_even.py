my_numbers=[1,2,3,4,5,6,7,8,9,10]
odd=[]
even=[]
sum = 0
total = 0
for x in my_numbers:
    if x % 2 != 0:
        odd.append(x)
        sum += x
    else:
        even.append(x)
        total += x
print(odd)
print(even)
print(sum)
print(total)