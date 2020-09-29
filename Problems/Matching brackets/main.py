# put your python code here
bracket = []
for val in input():
    if val == '(':
        bracket.append(val)
    elif val == ')':
        if bracket:
            bracket.pop()
        else:
            print('ERROR')
            break
else:
    print('ERROR' if bracket else 'OK')
