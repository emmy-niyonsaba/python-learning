# Question 4 (d): Mobile Money Transaction Record with keyboard input

customer_name = "Emmanuel Niyonsaba"
transaction_fee = 500

initial_balance = float(input("Enter initial balance (RWF): "))
withdrawal_amount = float(input("Enter withdrawal amount (RWF): "))

remaining_balance = initial_balance - withdrawal_amount - transaction_fee

print("\n===== TRANSACTION SUMMARY =====")
print("Customer:", customer_name)
print(f"Initial balance: {initial_balance:,.0f} RWF")
print(f"Withdrawal: {withdrawal_amount:,.0f} RWF")
print(f"Transaction fee: {transaction_fee:,} RWF")
print(f"Remaining balance: {remaining_balance:,.0f} RWF")
