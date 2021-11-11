import pickle
a = 10
b = 'abc'
c = '漢字'
with open('pics.pkl', 'wb') as f:
    pickle.dump([a,b,c], f)