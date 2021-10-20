n=input("整数を入力してください：")
n = int(n)
idx = 1
sum = 0
while idx <= n:
    sum += idx
    idx += 1
sum = str(sum)
print("1～5までの合計：" + sum)
sum = int(sum)
avg = sum / n
avg = str(avg)
print("平均：" + avg)