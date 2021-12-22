def str2int(s):
    """str2int 文字列を数値に変換した値を返す"""
    if(type(s) == str):
        if(s.isalpha() == True):
            return 0
    if(type(s) == str):
        if(s.isdigit() == True):
            return int(s)
    else:
        return s
print(str2int('a'))
print(str2int('10'))
print(str2int(100))