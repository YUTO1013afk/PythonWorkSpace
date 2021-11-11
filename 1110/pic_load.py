import pickle
with open('bignum.pkl', 'rb') as f:
    big_num = pickle.load(f)
    print(big_num)