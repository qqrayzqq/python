
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    sum = 0
    for score in student_marks[query_name]:
        sum += score
    average_score = sum / len(student_marks[query_name])
    print("{:.2f}".format(average_score))
