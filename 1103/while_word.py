import os
list = []
if os.path.exists("word.txt") == True:
    f = open('word.txt', 'r')
    list = f.readlines()
    for i, v in enumerate(list):
        list[i] = v.replace("\n", "")
    f.close()    
while True:
    n = input("単語を入力してください：")
    if n == "":
        print("終了します")
        break
    if n == "LIST":
        print("単語リスト：",end="")
        print(list)
    if n in list:
        print("すでに登録済です")
        continue
    if n != "LIST":
        list.append(n)
        file = open('word.txt', 'w')
        for d in list:
            file.write("%s\n" % d)
        file.close()
print("これまでに覚えた単語：",end="")
print(list)