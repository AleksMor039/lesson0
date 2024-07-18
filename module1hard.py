grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students=list(students)
students[0]='Aaron'
students[1]='Bilbo'
students[2]='Johnny'
students[3]='Khendrik'
students[4]='Steve'
print(students)
grades_1=sum(grades[0])
grades_1=grades_1/5
grades_2=sum(grades[1])
grades_2=grades_2/4
grades_3=sum(grades[2])
grades_3=grades_3/4
grades_4=sum(grades[3])
grades_4=grades_4/3
grades_5=sum(grades[4])
grades_5=grades_5/5
#
grades_all=grades_1, grades_2, grades_3, grades_4, grades_5
print(grades_all)
gpa={students[0]:grades_all[0], students[1]:grades_all[1], students[2]: grades_all[2], students[3]:grades_all[3], students[4]:grades_all[4]}
print(gpa)
