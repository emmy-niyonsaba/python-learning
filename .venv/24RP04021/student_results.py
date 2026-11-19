# Question 9: Student Examination Results

python_marks = 85
database_marks = 78
networking_marks = 92

total_marks = python_marks + database_marks + networking_marks
average_marks = total_marks / 3
average_text = str(average_marks)

print("Total marks:", total_marks)
print("Average marks:", average_marks)
print("The student's average mark is " + average_text + " out of 100.")

print("\ntotal_marks:", type(total_marks))
print("average_marks:", type(average_marks))
print("average_text:", type(average_text))
