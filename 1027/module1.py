import sys
idx = 0
while idx < 5:
    a = input("コマンドを入力してください：")
    if a == "終了":
        sys.exit()
    print("続く")
    idx += 1