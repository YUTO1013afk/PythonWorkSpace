def list2int(s):
    """list2int 文字列を数値に変換した値を返す（List 対応）"""
    if(type(s) == int):
        return s
    if(type(s) == str):
        if(s.isalpha() == True):
            return 0
    if(type(s) == str):
        if(s.isdigit() == True):
            return int(s)
    if(type(s) == list):
        for i in range(len(s)):
            if(type(s[i]) == str):
                if(s[i].isdigit() == True):
                    s[i] = int(s[i])
                elif(s[i].isalpha() == True):
                    s[i] = 0
        return s
    else:
        return None
print(list2int(['5','ab','100',10,1]))
print(list2int('100'))
print(list2int('xyz'))