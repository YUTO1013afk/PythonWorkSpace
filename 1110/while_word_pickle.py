import os
import pickle
list = []
if os.path.exists("word.txt") == True:
    with open('word.txt', 'rb') as f:
        x = pickle.load(f)
        list = x
for i, v in enumerate(list):
    list[i] = v.replace("\n", "")
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
        with open('word.txt', 'wb') as f:
            pickle.dump(list, f)
        for d in list:
            d = d.encode()
print("これまでに覚えた単語：",end="")
print(list)