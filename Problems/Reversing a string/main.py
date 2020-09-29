n = int(input())

my_stack = [input() for i in range(n)]
for _ in range(n):
    print(my_stack.pop())
