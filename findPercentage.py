if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    query_score= student_marks[query_name]
    print("%.2f" % round((query_score[0]+query_score[1]+query_score[2])/3, 2))
