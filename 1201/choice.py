def odd():
    print("奇数")
def even():
    print("偶数")
def choice_func(number):
    if(number%2==0):
        return even()
    else:
        return odd()
# main
while True:
    num = input("数字を入力してください。（0：終了）")
    if(num=="0"):
        break
    elif(num.isdigit()==False):
        print("入力が正しくありません")
        continue
    else:
        num = int(num)
        choice_func(num)