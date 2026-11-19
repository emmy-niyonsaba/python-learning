"""Question 5: Student Scholarship Eligibility System
"""


def read_percent(prompt):
    while True:
        try:
            value = float(input(prompt))
        except ValueError:
            print("Error: please enter a number.")
            continue
        if 0 <= value <= 100:
            return value
        print("Error: value must be between 0 and 100.")


def main():
    print("=== Scholarship Eligibility ===")
    average = read_percent("Average mark (0-100): ")
    attendance = read_percent("Attendance percentage (0-100): ")

    if average >= 85 and attendance >= 90:
        status = "FULL SCHOLARSHIP"
        reason = (f"Average {average} >= 85 and attendance {attendance}% >= 90%.")
    elif average >= 75 and attendance >= 80:
        status = "PARTIAL SCHOLARSHIP"
        reason = (f"Average {average} >= 75 and attendance {attendance}% >= 80%, "
                  "but the full-scholarship requirements (85 / 90%) are not met.")
    else:
        status = "NOT ELIGIBLE"
        problems = []
        if average < 75:
            problems.append(f"average {average} is below 75")
        if attendance < 80:
            problems.append(f"attendance {attendance}% is below 80%")
        if not problems:  # both individually fine but combination fails
            problems.append("the combination of average and attendance does not meet any rule")
        reason = "Because " + " and ".join(problems) + "."

    print(f"\nStatus     : {status}")
    print(f"Explanation: {reason}")


if __name__ == "__main__":
    main()
