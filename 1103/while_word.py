list = []
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
print("これまでに覚えた単語：",end="")
print(list)