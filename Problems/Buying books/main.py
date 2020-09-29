unread = []

for _ in range(int(input())):
    opt = input()
    if opt.startswith('BUY'):
        unread.append(opt.replace('BUY ', ''))
    if opt == 'READ':
        print(unread.pop())
