my_list = ['hello','nice','abc','test','morning','good','yes','world']
new_list = list(filter(lambda n : len(n)>=5, my_list))
print(my_list)
print(new_list)