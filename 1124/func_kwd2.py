def check_shopping(**kwargs):
    for key, value in dic_order.items():
        if value >= 100: 
            return True
        else:
            return False
# main  
dic_order = {}
while True:
    product_name = input('商品名を入力してください（0:終了）：')
    if product_name == '0':
        break
    product_price = input('金額を入力してください（0:終了）：')
    if product_price == '0':
        break
    elif product_price.isnumeric():
        product_price = int(product_price)
    else:
        print("数値以外が入力されました")
        continue

    dic_order[product_name] = product_price

if check_shopping(**dic_order):
    print('全てのデータは問題ありませんでした')
else:
    print('最低価格を下回った商品があります。')

for key, value in dic_order.items():
    print(f'{key} : {value}')