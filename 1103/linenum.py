import os
row_no = 0
fileobj = open("word.txt", "r")
while True:
    line = fileobj.readline()
    line = line.replace("\n", "")
    if line:
        row_no += 1
        print("000",end="")
        row_no = str(row_no)
        print(row_no + ":" + line)
        row_no = int(row_no)