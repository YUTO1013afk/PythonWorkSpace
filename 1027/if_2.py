while True:
    n = input("好きな文字を入力してください：")
    if(n == ""):
        break
    elif(n.isdigit() == True):
        print("数字")
    elif(n.isalpha() == True):
        print("アルファベット")
    elif(n.isalnum() == True):
        print("アルファベットと数字")
    else:
        print("その他")