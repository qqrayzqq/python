M = int(input())
l_ = set(map(int, input().split()))
N = int(input())
for _ in range(N):
    inp = list(input().split())
    if inp[0] == 'pop':
        l_.pop()
    elif inp[0] == 'remove':
        l_.remove(int(inp[1]))
    elif inp[0] == 'discard':
        l_.discard(int(inp[1]))
print(sum(l_))
