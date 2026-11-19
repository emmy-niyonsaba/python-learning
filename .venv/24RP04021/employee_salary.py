# Question 5: Employee Salary Management

employee_name = "Emmanuel Niyonsaba"
basic_salary = 250000
transport_allowance = 30000
housing_allowance = 50000

gross_salary = basic_salary + transport_allowance + housing_allowance

print("===== SALARY SUMMARY =====")
print("Employee:", employee_name)
print(f"Basic salary: {basic_salary:,} RWF")
print(f"Transport allowance: {transport_allowance:,} RWF")
print(f"Housing allowance: {housing_allowance:,} RWF")
print(f"Gross salary: {gross_salary:,} RWF")

# d) Separate declarations: each variable gets its own statement.
#    basic = 250000
#    transport = 30000
#    housing = 50000
#
#    Multiple assignment: several variables are assigned in one statement.
#    basic, transport, housing = 250000, 30000, 50000
#    Or one value to many variables: a = b = c = 0
#
#    Separate declarations are clearer for many or complex values;
#    multiple assignment is shorter for related values.
