# Question 3: Debugging a Python Program
#
# a) Errors in the original program:
#    1. "if marks >= 50:" is followed by print("Passed") with no indentation
#       (IndentationError).
#    2. "else" is missing the colon ':' (SyntaxError).
#    3. print("Failed") is indented inconsistently with print("Passed")
#       and the if/else block structure.
#
# c) Indentation in Python defines code blocks. Unlike other languages that
#    use braces, Python uses indentation to know which statements belong to
#    an if, else, loop or function. Wrong indentation causes errors or
#    changes the program's behaviour.
#
# d) Expected output:
#    Student: Emmanuel Niyonsaba
#    Passed

# b) Corrected program
student_name = "Emmanuel Niyonsaba"
marks = 85

print("Student:", student_name)
if marks >= 50:
    print("Passed")
else:
    print("Failed")
