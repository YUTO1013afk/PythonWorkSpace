# 関数を辞書で渡し、実行する
def func1():
    print("Hello")
def func2():
    print("Goodbye")
# main
run_list = {'a': func1, 'b': func2}
print("a=>Hello,","b=>Goodbye")
key = input("どちらを実行しますか？:")
while key!= "":
    try:
        run_list[key]()
        print("a=>Hello,","b=>Goodbye")
        key = input("どちらを実行しますか？:")
    except KeyError:
        print("どちらかを選択してください。")
        print("a=>Hello,","b=>Goodbye")
        key = input("どちらを実行しますか？:")