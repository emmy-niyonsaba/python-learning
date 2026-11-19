"""Question 1: Mobile Money Transaction Management System
"""

TRANSFER_FEE = 1000


def read_amount(prompt):
    """Read a positive number from the user; keep asking until valid."""
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                print("Error: amount must be greater than zero.")
                continue
            return value
        except ValueError:
            print("Error: please enter a valid number.")


def main():
    initial_balance = 250_000
    deposit = 75_000
    withdrawal = 80_000
    transfer = 45_000

    balance = initial_balance
    log = []  # (description, amount, fee, balance after)

    # a) + c) process each transaction using assignment operators
    balance += deposit
    log.append(("Deposit", deposit, 0, balance))

    if balance >= withdrawal:
        balance -= withdrawal
        log.append(("Withdrawal", withdrawal, 0, balance))
    else:
        print("Withdrawal of 80,000 RWF failed: insufficient funds.")

    if balance >= transfer + TRANSFER_FEE:
        balance -= transfer
        balance -= TRANSFER_FEE
        log.append(("Transfer", transfer, TRANSFER_FEE, balance))
    else:
        print("Transfer failed: insufficient funds (amount + fee).")

    # b) additional withdrawal check with comparison + logical operators
    print(f"\nCurrent balance: {balance:,.0f} RWF")
    extra = read_amount("Enter an additional withdrawal amount (RWF): ")
    if extra > 0 and extra <= balance:
        balance -= extra
        log.append(("Additional withdrawal", extra, 0, balance))
        print("Additional withdrawal approved.")
    else:
        print(f"Additional withdrawal DENIED: {extra:,.0f} RWF exceeds "
              f"the available balance of {balance:,.0f} RWF.")

    # d) detailed summary
    total_fees = sum(item[2] for item in log)
    print("\n" + "=" * 62)
    print("TRANSACTION SUMMARY")
    print("=" * 62)
    print(f"Initial balance: {initial_balance:>12,.0f} RWF")
    print("-" * 62)
    print(f"{'Transaction':<24}{'Amount':>12}{'Fee':>8}{'Balance':>16}")
    for name, amount, fee, bal in log:
        print(f"{name:<24}{amount:>12,.0f}{fee:>8,.0f}{bal:>16,.0f}")
    print("-" * 62)
    print(f"Total fees charged: {total_fees:>10,.0f} RWF")
    print(f"Final balance:      {balance:>10,.0f} RWF")
    print("=" * 62)


if __name__ == "__main__":
    main()
