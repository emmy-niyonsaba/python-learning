# Question 8: Agricultural Production Records

crop_name = "Maize"        # str
quantity_kg = 1200         # int
price_per_kg = 450.5       # float
is_sold = False            # bool

total_revenue = quantity_kg * price_per_kg

print("Crop:", crop_name)
print("Quantity (kg):", quantity_kg)
print("Price per kg (RWF):", price_per_kg)
print("Sold:", is_sold)
print(f"Total expected revenue: {total_revenue:,.2f} RWF")

print("\ncrop_name:", type(crop_name))
print("quantity_kg:", type(quantity_kg))
print("price_per_kg:", type(price_per_kg))
print("is_sold:", type(is_sold))

# d) Integer (int): whole numbers, e.g. quantity_kg = 1200.
#    Floating-point (float): numbers with decimals, e.g. price_per_kg = 450.5.
#    String (str): text, e.g. crop_name = "Maize".
#    Boolean (bool): True or False, e.g. is_sold = False.
