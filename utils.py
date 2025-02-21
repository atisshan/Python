def findmax():
    numbers =[9,20,3,7]
    max = numbers[0]
    for item in numbers:
        if item > max:
            max = item
    print(max) 