import time

def run_time(func):
    def count(*args,**kwargs):
        start_time = time.time()
        reslut = func(*args,**kwargs)
        print('実行関数:' + func.__name__ + " ", end="")
        print('実行時間：{:.15f}'.format(time.time() - start_time))
        return reslut
    return count

# main
@run_time
def test(n):
    for i in range(n):
        time.sleep(i)

test(3)
test(5)