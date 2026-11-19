"""Question 6: Bank Loan Eligibility Assessment
"""

MIN_AGE = 21
MIN_INCOME = 200_000
MIN_YEARS = 2


def read_number(prompt, integer=False, allow_negative=False):
    while True:
        try:
            value = int(input(prompt)) if integer else float(input(prompt))
        except ValueError:
            print("Error: please enter a valid number.")
            continue
        if not allow_negative and value < 0:
            print("Error: negative values are not allowed.")
            continue
        return value


def read_yes_no(prompt):
    while True:
        answer = input(prompt).strip().lower()
        if answer in ("yes", "y"):
            return True
        if answer in ("no", "n"):
            return False
        print("Error: please answer yes or no.")


def main():
    print("=== Loan Eligibility Screening ===")
    name = input("Customer name: ").strip() or "Customer"
    age = read_number("Age (years): ", integer=True)
    income = read_number("Monthly income (RWF): ")
    years = read_number("Years of employment: ")
    has_default = read_yes_no("Any outstanding defaulted loan? (yes/no): ")

    reasons = []
    if age < MIN_AGE:
        reasons.append(f"Age {age} is below the minimum of {MIN_AGE}.")
    if income < MIN_INCOME:
        reasons.append(f"Monthly income {income:,.0f} RWF is below {MIN_INCOME:,} RWF.")
    if years < MIN_YEARS:
        reasons.append(f"Employment of {years} year(s) is below {MIN_YEARS} years.")
    if has_default:
        reasons.append("Customer has an outstanding defaulted loan.")

    print(f"\nResult for {name}:")
    if age >= MIN_AGE and income >= MIN_INCOME and years >= MIN_YEARS and not has_default:
        print("QUALIFIED: all loan conditions are satisfied.")
    else:
        print("NOT QUALIFIED. Reasons:")
        for r in reasons:
            print(" -", r)


if __name__ == "__main__":
    main()
