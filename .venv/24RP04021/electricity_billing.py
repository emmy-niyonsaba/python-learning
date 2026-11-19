# Electricity Billing System

units = float(input("Enter electricity units consumed: "))

# Assumed rate per unit for this exercise
rate_per_unit = 250

# Total cost = units x rate
total_bill = units * rate_per_unit

print("Units consumed:", units)
print(f"Rate per unit: {rate_per_unit:,} RWF")
print(f"Estimated bill: {total_bill:,.0f} RWF")
