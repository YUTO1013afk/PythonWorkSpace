sym = ["+","-","*","/"]
result = []
while True:
    calc = input("calc :")
    if (calc == "="):
        break
    elif (calc.isdigit() == False):
        if (calc not in sym):
            print("入力が正しくありません。")
            continue
    elif (len(result) > 0):
        if (str(result[-1]).isdigit() == True and calc.isdigit() == True):
            print("入力が正しくありません。")
            continue 
    result.append(calc)
    if (result[0] in sym):
        print("入力が正しくありません。")
        result.clear()
        continue
    elif (len(result) > 1):
        if (result[-2] in sym and calc in sym):
            print("入力が正しくありません。")
            del result[-1]
            continue
print("入力した計算式：", end="")
for i in range(len(result)):
    print(result[i], end="")
    sum = (''.join(result))
print()
print("計算結果：" + str(int(eval(sum))))