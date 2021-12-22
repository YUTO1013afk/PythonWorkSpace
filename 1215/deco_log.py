import datetime

def log_file(func):
    def function(*args,**kwargs):
        with open('python.log', 'a') as f:
            reslut = func(*args,**kwargs)
            f.write(str(datetime.datetime.now()) + " ")
            f.write('function:' + func.__name__ + " ")
            f.write("args:" + str(args) + " ")
            f.write("kwargs:" + str(kwargs) + "\n")
            return reslut
    return function

# main
@log_file
def test(n):
    print('test->{}'.format(n))

# 呼出
test(100)

# 呼出
for i in range(5):
    test(i)