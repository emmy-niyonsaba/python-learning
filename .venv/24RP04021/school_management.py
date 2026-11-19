# Question 6: Local and Global Variables in School Management

school_name = "RP-Tumba College"
academic_year = 2025


def display_department():
    department_name = "Information Technology"
    student_population = 320
    print("School:", school_name)
    print("Department:", department_name)
    print("Student population:", student_population)


def update_academic_year():
    global academic_year
    academic_year = 2026


display_department()

print("\nAcademic year before:", academic_year)
update_academic_year()
print("Academic year after:", academic_year)

# d) A global variable is declared outside functions and can be read by any
#    function (e.g. school_name). A local variable is declared inside a
#    function and exists only while that function runs (e.g. department_name
#    inside display_department()); using it outside raises a NameError.
#    To modify a global variable inside a function, the 'global' keyword is
#    required, as in update_academic_year().
