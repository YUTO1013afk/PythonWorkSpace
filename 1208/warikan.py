import math
def input_int(message):
    return int(message)
def calc_payment(sum,num):
    pay = math.ceil((sum / num) / 100) * 100 
    balance = sum - pay * (num-1)
    return [pay,balance]
def output_payment(payment,num):
    num -= 1
    print(f'支払金額：' + str("{:,d}".format(payment[0])) + "円" + " (" + str(num) + "人)")
    print(f'幹事金額：' + str("{:,d}".format(payment[1])) + "円")
#main
sum = input_int(input("支払合計金額を入力してください："))
num = input_int(input("参加者人数を入力してください："))
payment = calc_payment(sum,num)
output_payment(payment,num)