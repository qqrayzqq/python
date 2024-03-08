students = [("Squidward", "F", 30), ("Sandy", "A", 33), ("Patrick", "D", 36), ("Spongebob", "B", 20)]
grade = lambda grade: grade[1]
age = lambda age: age[2]
students.sort(key=grade)
students.sort(key=age, reverse=True)
for student in students:
    print(student)
