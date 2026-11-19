# Question 4 (a-c): Mobile Money Transaction Record with declared values

customer_name = "Emmanuel Niyonsaba"
initial_balance = 150000
withdrawal_amount = 45000
transaction_fee = 500

remaining_balance = initial_balance - withdrawal_amount - transaction_fee

print("===== TRANSACTION SUMMARY =====")
print("Customer:", customer_name)
print(f"Initial balance: {initial_balance:,} RWF")
print(f"Withdrawal: {withdrawal_amount:,} RWF")
print(f"Transaction fee: {transaction_fee:,} RWF")
print(f"Remaining balance: {remaining_balance:,} RWF")
