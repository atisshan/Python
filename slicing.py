my_list=[1,2,3,4,5]
my_sublist=[0,1,2,3,4]
sum=0
total = 0
if len(my_list) == len(my_sublist):
    total += my_list[0:5] + my_sublist[0:5]
    sum += total
    print(sum)
