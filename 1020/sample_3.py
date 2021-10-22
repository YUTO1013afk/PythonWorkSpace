# 初期化
marks = ('S','H','C','D') # 4 種類のマーク
cards = [1,2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13] # デッキ用リスト
card = [(mark, card) for mark in marks for card in cards]
print('-'*10)
print(card)
print('-'*10)
# 1 枚選択
import random # 乱数用モジュール
r = random.randrange(52) # 0〜51 の乱数生成
print(f'選んだカードは{card[r]}です')