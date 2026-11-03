# Reflection 1:
# I would use .get() when a key might be missing and I want the program to keep running
# with a default value. I would use bracket notation when I expect the key to exist
# and need its value. My rule is to use .get() for optional information and [] for required information.
#
# Reflection 2:
# This pattern reminds me of using SUMIF or a PivotTable in Excel to total values by category.
# Python is more useful for large datasets because it can automatically repeat calculations
# across many records and can be customized for more complicated tasks.
# Exercise 1 - One Customer

customer = {"name": "Alice", "email": "alice@email.com", "tier": "gold", "ytd_spend": 1200}

print(customer["name"])
print(customer["email"])
print(customer["tier"])
print(customer["ytd_spend"])

print(customer)

# Exercise 2 - Update and Add

customer["phone"] = "555-123-4567"

print(customer)

customer["tier"] = "platinum"

print(customer)

del customer["email"]

print(customer)

# Exercise 3 - Safe Lookup

email = customer.get("email", "no email on file")
print(email)

try:
    print(customer["email"])
except KeyError:
    print("KeyError: email key not found")

    # Exercise 4 - Iterate

for key, value in customer.items():
    print(f"{key}: {value}")

# Without .items(), the loop only gives us the keys.
for key in customer:
    print(key)

    # Exercise 5 - Lookup Table

tier_discounts = {
    "bronze": 0,
    "silver": 0.05,
    "gold": 0.10,
    "platinum": 0.15
}

discount_rate = tier_discounts.get(customer["tier"], 0)

purchase = 200
discount_amount = purchase * discount_rate
final_price = purchase - discount_amount

print("Tier:", customer["tier"])
print("Discount rate:", discount_rate * 100, "%")
print("Final price: $", final_price)

# Exercise 6 - List of Dictionaries

dict1 = {"name": "Alice", "tier": "platinum"}
dict2 = {"name": "Bob", "tier": "gold"}
dict3 = {"name": "Charlie", "tier": "silver"}

customers = [dict1, dict2, dict3]

for customer_info in customers:
    tier = customer_info["tier"]
    discount_rate = tier_discounts.get(tier, 0)
    discount_amount = 300 * discount_rate

    print(f"{customer_info['name']} | {tier} | Discount: ${discount_amount:.2f}")

    # Exercise 7 - Nested Catalog
catalog = {
    "Widget A": {"price": 9.99, "stock": 150},
    "Gadget C": {"price": 49.99, "stock": 8}
}

for product_name, details in catalog.items():
    if details["stock"] < 20:
        print(f"LOW STOCK: {product_name} - only {details['stock']} left")

        # Exercise 8 - Sales by Region
transactions = [
    {"region": "South", "amount": 300},
    {"region": "North", "amount": 150},
    {"region": "South", "amount": 200}
]

sales_by_region = {}

for transaction in transactions:
    region = transaction["region"]
    amount = transaction["amount"]
    sales_by_region[region] = sales_by_region.get(region, 0) + amount

for region in sorted(sales_by_region):
    print(f"{region}: {sales_by_region[region]}")