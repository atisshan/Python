weight=int(input('weight:'))
put=input('Lb(s) or k(g):')
if (put == 'l' or put == 'L'):
    j= weight * 0.45
    print(f'{j} kilos')
else:
    x = weight // 0.45
    print(f'{x} pounds')