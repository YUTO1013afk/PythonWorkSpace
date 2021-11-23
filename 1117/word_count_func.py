import re
f = open('sentence.txt')
data = f.read()
f.close

# counting
words = {}
data = re.split(r'\s+|\,|\.|\(|\)|\"|\:', data.lower())
for item in data:
    if len(item)-1 < 1:  
        data.remove("")
data.sort()
for word in data:
    words[word] = words.get(word, 0) + 1

# sort by count
d = [(v,k) for k,v in words.items()]
for count, word in d[:]:
    print('%s :%d' % (word, count))