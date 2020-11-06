# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
print(student_heights)
# 🚨 Don't change the code above 👆

# Write your code below this row 👇
sum_of_students = 0
counter = 0
for student in student_heights:
  sum_of_students += student 
  counter += 1

average = round(sum_of_students / counter)
print(average)


