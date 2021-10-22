fruits = ['バナナ','リンゴ','オレンジ']
while True:
    n = input("果物をカタカナで入力してください：")
    if (n == ""):
        break
    if (n in fruits):
        print(n + "は、知っています！")
    else:
        print(n + "は、知りませんでした。覚えておきます。")
        fruits.append(n)
print('知っている果物')
print(fruits)