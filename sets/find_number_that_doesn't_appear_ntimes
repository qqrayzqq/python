n = int(input())
l = input().split()
l.sort()

for i in range(0, len(l), n):
    if i + n > len(l) or l[i] != l[i + n - 1]:
        print(l[i])
        break
