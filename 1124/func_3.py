def do_anything(*args):
    '''引数の個数によって何かする。int と str で動作'''
    args_count = len(args)
    if(args_count == 0):
        print("受け取った値：",args[:])
        return print("やること無いので暇です")
    if(args_count == 1):
        if(type(args[0]) == str):
            print("受け取った値：",(args[:]))
            print(args[0]*2)
        elif(type(args[0]) == int):
            print("受け取った値：",(args[:]))
            print(args[0]*2)
        else:
            print("受け取った値：",(args[:]))
            return print("難しくて無理です")
    elif(args_count == 2):
        if(type(args[0]) == int):
            if(type(args[1]) == str):
                print("受け取った値：",args[:])
                print("できません〜")
            elif(type(args[1]) == int):
                print("受け取った値：",args[:])
                print(args[0] + args[1])
        if(type(args[0]) == str):
            if(type(args[1]) == str):
                print("受け取った値：",args[:])
                print(args[0] + args[1])
        elif(type(args[0]) == list):
            if(type(args[1]) == list):
                print("受け取った値：",args[:])
                print("無茶言わないで！")
    else:
        print("受け取った値：",args[:])
        print("無理です...")
# main
do_anything()
do_anything(10)
do_anything('asdfg')
do_anything([1,2,3])
do_anything(10,20)
do_anything(10,'abc')
do_anything('x','yz')
do_anything([1,2,3],[4,5,6])
do_anything(1,2,3)