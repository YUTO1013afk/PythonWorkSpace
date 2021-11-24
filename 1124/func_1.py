def combine_list(list1, list2):
    '''2 つのリストを結合し、リストで返す'''
    if(type(list1) == list):
        if(type(list2) == list):
            return list1 + list2
    if(type(list1) == list):
        if(type(list2) == str):
            print("引数がリストではありません")
            list0 = []
            list0.append(list1)
            list0.append(list2)
            return list0
    if(type(list2) == list):
        if(type(list1) == str):
            print("引数がリストではありません")
            list4 = []
            list4.append(list1)
            list4.append(list2)
            return list4
    if(type(list1) == int):
        if(type(list2) == str):
            print("引数がリストではありません")
            list3 = []
            list3.append(list1)
            list3.append(list2)
            return list3
# main
# 正常な引数
print(combine_list([1, 2, 3], [4, 5, 6]))
print(combine_list(list2=[1, 2, 3], list1=[4, 5, 6]))
# 誤った引数
print(combine_list('a', [1, 2, 3]))
print(combine_list([1, 2, 3], 'xyz'))
print(combine_list(10, 'abc'))