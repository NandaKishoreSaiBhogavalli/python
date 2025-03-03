n = int(input().strip())     #taking input, for the range of name and grades
student_names = []

for i in range(n):
    names = " ".join(input().strip().split())  #converting name into a string because bydefault when appending it into student_names it is taking name as a separate list
    grades = float(input().strip())
    student_names.append([names, grades])#appending names,grades into student_names as [[name1,grade1],[name2],[grade2]]

sorted_grades = sorted(set(x[1] for x in student_names))   # we are extracting grades from student_names which are at index1 and converting into sets to eliminate duplicates and sorting grades
if len(sorted_grades) > 1:     # this is a edge case handling so when grades len is greater than 1 then only we can retrieve the second lowest grade
    second_lowest = sorted_grades[1]
else:
    pass
top2 = [students[0] for students in student_names if students[1] == second_lowest]   # we are retreiving the student names by matching with secondlowest grade

sorted_top2 = sorted(top2)     #sorting names alphabetically and printing
for name in sorted_top2:
    print(name)