n = int(input())

for i in range(1, n + 1):
    print(' ' * (i - 1), end='')
    print('*' * (n + 1 - i))