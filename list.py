my_list=[1,2,3,4,5]
my_sublist=[0,1,2,3,4]
sum=[]
if len(my_list) == len(my_sublist):
    for i in range (len(my_list)):
        sum.append(my_list[i] + my_sublist[i])
    print(sum)