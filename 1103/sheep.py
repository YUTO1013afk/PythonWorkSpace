import time
n = input("何匹数えますか？：")
n = int(n)
sheep = 0
while sheep < n:
    if n > 100:
        break
    sheep += 1
    time.sleep(sheep)
    sheep = str(sheep)
    print("羊が" + sheep + "匹")
    sheep = int(sheep)