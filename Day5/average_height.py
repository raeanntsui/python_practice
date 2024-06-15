# Input a Python list of student heights
student_heights = [156, 178, 165, 171, 187]
# 🚨 Don't change the code above 👆
  
# Write your code below this row 👇
total_height = 0
number_of_students = 0
for height in student_heights:
  total_height += height
  # print(f"total_height Height is now: {total_height}")
  number_of_students += 1
  # print(f"Number of students is now: {number_of_students}")

# print(f"Current total_height height = {total_height}")
average = total_height / number_of_students
print(f"total_height height = {total_height}")
print(f"number of students = {number_of_students}")
print(f"average height = {round(average)}")