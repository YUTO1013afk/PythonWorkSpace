def any_items(*args):
    items_count = len(args)
    print(f'引数は{items_count}個です。受け取った値は{args}です')
any_items()
any_items(10)
any_items(10, 20)
any_items(10, 'a', 'xyz')
any_items(10, [1, 2, 3])