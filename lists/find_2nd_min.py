if __name__ == '__main__':
    l = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        l.append([name, score])
    l.sort()
    min_1 = 1000
    min_2 = 1000
    for i in l:
        if i[1] < min_1:
            min_2 = min_1
            min_1 = i[1]
        elif min_2 > i[1] != min_1:
            min_2 = i[1]
    for i in l:
        if i[1] == min_2:
            print(i[0])
