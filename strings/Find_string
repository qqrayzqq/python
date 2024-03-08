
def count_substring(str_, sub_str):
    cnt = 0
    for char in range(0, len(str_) - len(sub_str) + 1):
        if str_[char:char+len(sub_str)] == sub_str:
            cnt += 1

    return cnt


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    count = count_substring(string, sub_string)
    print(count)
