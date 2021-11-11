DATA_FILENAME = 'test.csv'
person_data = []

# fileの読み込み
with open(DATA_FILENAME, 'r', encoding='utf-8') as f:
    title = f.readline().strip().split(',')         # 1行目を読み込み
    for line in f:                                  # 残りの行を全て読み込み
        person_data.append(line.strip().split(','))

print('person dataは',person_data)

col = 1                                             # [0]は名前なのでSkip [1]から
avg = [0] * len(title)                              # 平均を格納するリスト
while col < len(title):
    for score in person_data:                       # 全員分の科目得点の処理
        avg[col] += int(score[col])/len(person_data)
    col += 1                                        # 次の科目

print(title[1:])
print(avg[1:])