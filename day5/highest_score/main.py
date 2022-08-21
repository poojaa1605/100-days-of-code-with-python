# Average height exercise

student_heights = input("Input a list of student's height    ").split()

for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
print(student_heights)

total_heights = 0

for height in student_heights:
    total_heights += height

number_of_students = 0

for student in student_heights:
    number_of_students += 1

average_height = round(total_heights / number_of_students)

print(f"Average: {average_height}")
