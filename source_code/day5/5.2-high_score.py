# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆

# Cannot use the following Code
# print(max(student_scores))
# print(min(student_scores))

# for score in student_scores:

# print("The highest score in the class is: " + )

# student_scores.sort()

#Write your code below this row 👇

# print(student_scores.sort())
# print(student_scores.pop())
# print(student_scores)
highest_score = 0
for score in student_scores:
    if score > highest_score:
        highest_score = score
print(f"The highest score in the class is: {highest_score}")