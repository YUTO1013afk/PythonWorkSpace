import pickle
with open('pics.pkl', 'rb') as f:
    x = pickle.load(f)
print(x)