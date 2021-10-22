data = [10, 1, 0, 30, 1, 20, 0, 5, 0, 60]
# この中から、目的の要素を全て削除する。
# [10, 1, 30, 1, 20, 5, 60] ← ほしい結果
ng = 0 # 不要なデータ
data = [item for item in data if item != ng]  # 取り除く＝それ以外を残す
print(data)