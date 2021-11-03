a = 0
while a < 10:
    a += 1
    if a == 5:
        continue
else:
    print(a, "else!")
print(a, "finish")