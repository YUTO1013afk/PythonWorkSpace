import csv
### CSVファイル読み込み
with open('test.csv', newline='', encoding="utf8") as csvfile:
    ### CSVオブジェクト作成
    csvreader = csv.reader(csvfile)
    line = [row for row in csvreader]
    i = 1
    while i <= 4:
        sum = 0
        sum = int(line[i][1]) + int(line[i][2]) + int(line[i][3]) + int(line[i][4])
        print(line[i][0] + " ", end="")
        print(sum)
        i += 1