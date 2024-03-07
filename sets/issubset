s_ = set(input().split())
M = int(input())
flag = True
for _ in range(M):
    c_ = set(input().split())
    if len(c_) < len(s_):
        if not c_.issubset(s_):
            print("False")
            flag = False
            break
    else:
        print("False")
        flag = False
        break
if flag:
    print("True")
