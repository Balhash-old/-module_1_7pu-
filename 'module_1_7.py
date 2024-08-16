grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
average=[[0], [1], [2], [3], [4]]
average[0] = sum(grades[0]) / len(grades[0])
average[1] = sum(grades[1]) / len(grades[1])
average[2] = sum(grades[2]) / len(grades[2])
average[3] = sum(grades[3]) / len(grades[3])
average[4] = sum(grades[4]) / len(grades[4])
print(average[0:])
students={'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
my_list=list(students)
sorted_list=sorted(my_list)
print(sorted_list)
new_dict=dict()
print(dict(zip(sorted_list, average)))