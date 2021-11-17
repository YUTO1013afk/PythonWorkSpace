# list を利用
products = ['orange', 'apple', 'banana']
price = [100, 150, 180]

print('商品名¥t 価格')
for i in range(3):
    print('{}¥t{}'.format(products[i], price[i]))

# dic を利用
products_price = {'orange': 100, 'apple': 150, 'banana': 180}

print('商品名¥t 価格')
for i in products_price:
    print('{}¥t{}'.format(i, products_price[i]))
