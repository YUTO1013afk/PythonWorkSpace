import sys
argv = sys.argv
if (len(argv) == 1):
    print("引数なし")
else:
    print("引数：",str(argv))
row_no = 0
idx = 1
while idx <= len(argv)-1:
    print("-"*3,str(argv[idx]),"-"*3)
    fileobj = open(argv[idx], "r", encoding="utf8")
    line = fileobj.readline()
    line = line.rstrip("\n")
    while line:
        row_no += 1
        row_no = str(row_no)
        print("000" + row_no + ":" + line)
        row_no = int(row_no)
        line = fileobj.readline()
        line = line.rstrip("\n")
        continue
    idx += 1
    row_no = 0