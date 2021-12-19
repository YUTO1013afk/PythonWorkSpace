sym = ["+","-","*","/"]
paren = ["(",")"]
result = []
while True:
    calc = input("calc :")
    if (calc == "="):
        if (result.count("(") == result.count(")")):
            if (result[0] == "(" and result[-1] == ")"):
                break
        elif (any('(' in item for item in result) == False):
            break
        elif ((result.count("(") + result.count(")")) % 2 != 0 and result[-1] == ")" and result[-2] in sym):
            del result[-1]
            break
        elif (result.count("(") > result.count(")")):
            count = result.count("(") - result.count(")")
            for i in range(count):
                result.append(")")
            break
        else:
            count = result.count(")") - result.count("(")
            for i in range(count):
                result.insert(0,"(")
            break
    result.append(calc)
    if (calc.isdigit() == False):
        if (calc not in sym and calc not in paren):
            if (calc == "="):
                break
            print("入力が正しくありません。")
            del result[-1]
            continue
        if (len(result) == 1):
            if (calc in sym and str(result[-1]).isdigit() == False):
                print("数値を入力してください。")
                del result[-1]
                continue
        if (len(result) == 1):
            if (calc == ")"): 
                print("入力が正しくありません。")
                del result[-1]
                continue
    if (len(result) > 1):
        if (str(result[-2]).isdigit() == True and calc.isdigit() == True):
            print("入力が正しくありません。")
            del result[-1]
            continue
        elif (result[-2] == "(" and str(result[-1]).isdigit() == False and calc in sym):
            print("数値を入力してください。")
            del result[-1]
            continue
        elif (result[-2] == "(" and calc == "("):
            print("数値を入力してください。")
            del result[-1]
            continue  
    if (len(result) > 1):
        if (calc == ")" and calc in sym and calc != "*"):
            if (str(result[-2]).isdigit() == False):
                print("入力が正しくありません。")
                del result[-1]
                continue
        if (result[-2] in sym and calc in sym):
            if (result[-2] != "*"):
                print("入力が正しくありません。")
                del result[-1]
                continue
        if (result[-2] == "/" and calc == "0"):
            print("除算できません。")
            del result[-1]
            continue
        elif (result[-2] in sym and calc == ")"):
            print("数値を入力してください。")
            del result[-1]
            continue
    if (len(result) > 2):
        if (result[-3] in paren and calc in paren and str(result[-2]).isdigit() == True):
            print("入力が正しくありません。")
            del result[-1]
            continue
        elif (result[-3] == "*" and result[-2] == "*" and calc == "*"):
            print("入力が正しくありません。")
            del result[-1]
            continue
        elif (result[-3] == ")" and calc.isdigit() == True or calc == "("):
            if (result[-2] not in sym):
                print("演算子を入力してください。")
                del result[-1]
                continue
        elif (result[-2] not in sym and str(result[-2]).isdigit() == True and calc == "("):
            print("演算子を入力してください。")
            del result[-1]
            continue
if (result[-1] == "="):
    del result[-1]
elif (result[-2] == ")"):
    del result[0]
    del result[-1]
print("入力した計算式：", end="")
for i in range(len(result)):
    print(result[i], end="")
    sum = (''.join(result))
print()
print("計算結果：" + str(int(eval(sum))))