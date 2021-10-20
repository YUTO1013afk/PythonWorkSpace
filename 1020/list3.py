a=[0,1,2,3,4,5]
b=['a','b']
c=['X','y','z']

print(a)

d=a[:]  #aのコピーを作成
d[1:2]=b[:]
print(d)
d[4:5]=c[:]
print(d)