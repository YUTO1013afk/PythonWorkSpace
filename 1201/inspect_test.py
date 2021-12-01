import inspect
def func():
    pass
result = inspect.getmembers(func)
for k, v in result:
    print(f'{k}=>{v}')