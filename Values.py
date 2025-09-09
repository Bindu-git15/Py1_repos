# Given list of student marks
marks = [95, 88, 76, 67, 89, 92]

# Unpacking into topper, others, and last student
topper, *others, last_student = marks

print("Topper:", topper)
print("Others:", others)
print("Last Student:", last_student)

