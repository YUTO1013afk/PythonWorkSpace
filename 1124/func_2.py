def tax_included(price,tax=0.1):
    if(tax < 0):
        sum = None
        tax = tax * 100
        tax = int(tax)
        return print(f'{price}の消費税{tax}%の税込金額は{sum}円')
    elif(tax < 0.1):
        sum = price * (tax + 1)
        sum = int(sum)
        tax = tax * 100
        tax = int(tax)
        return print(f'{price}の消費税{tax}%の税込金額は{sum}円')
    else:
        sum = price * (tax + 1)
        sum = int(sum)
        return print(f'{price}の税込金額は{sum}円')
tax_included(5000)
tax_included(5000,0.08)
tax_included(5000,-0.05)