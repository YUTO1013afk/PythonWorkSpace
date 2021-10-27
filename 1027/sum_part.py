i = input("数字1：")
j = input("数字2：")
i = int(i)
j = int(j)
sum = 0
for a in range(i,j):
    sum += a
sum += j
i = str(i)
j = str(j)
print(i + "から" + j + "までの合計は",end="")
print(sum,end="")
print("です")