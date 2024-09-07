def custom_append(my_lst, value):
    new_list=[0]*(len(my_list)+1)
    for i in range(len(my_list)):
        new_list[i]=my_list[i]
    new_list[-1]=value
    return new_list
my_list = [1,2,3,4,5,6,7,8,9]
updated_list=custom_append(my_list, 10)
print(updated_list) 