list=[1,1,8,9]
unique =[]
for item in list:
    if item not in unique:
        unique.append(item)
print(unique)