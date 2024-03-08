M = int(input())
l_ = set(map(int, input().split()))
N = int(input())
l_1 = set(map(int, input().split()))
L_ = list(l_.difference(l_1)) + list(l_1.difference(l_))
L_.sort()
for i in L_:
    print(i)
