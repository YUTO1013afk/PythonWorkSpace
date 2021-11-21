import os
word = []
f = open('word_list.txt', 'r')
for i in f:
    word.append(i.rstrip('\n'))
f.close
word_count = {}
word = sorted(word)
for j in word:
    if j in word_count:
        word_count[j] += 1
    else:
        word_count[j] = 1
for i in word_count:    
    print('%s :%d' % (i, word_count[i]))