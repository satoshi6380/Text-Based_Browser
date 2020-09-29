from collections import deque

stack = deque()
for _ in range(int(input())):
    val = input().split(' ')
    if val[0] == 'PUSH':
        stack.append(val[1])
    elif val[0] == 'POP':
        stack.pop()

print('\n'.join(reversed(stack)))
