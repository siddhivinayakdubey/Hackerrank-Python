def average(x,y,z):
    m= (x+y+z)/3
    return ("{:.2f}".format(m))
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for i in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

    print(average(student_marks[query_name][0], student_marks[query_name][1], student_marks[query_name][2]))
