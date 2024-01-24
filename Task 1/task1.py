def validate_yes_no_input(prompt):
    while True:
        user_input = input(prompt).strip().upper()
        if user_input not in ('Y', 'N'):
            print('Please answer "Y" or "N".')
        else:
            return user_input == 'Y'

while True:
    num_pizzas_str = input("How many pizzas ordered? ")
    if not num_pizzas_str.isdigit():
        print("Please enter a valid positive integer!")
        continue

    num_pizzas = int(num_pizzas_str)
    if num_pizzas <= 0:
        print("Please enter a valid number!")
        continue

    delivery_required = validate_yes_no_input("Is delivery required? (Y/N) ")
    is_tuesday = validate_yes_no_input("Is it Tuesday? (Y/N) ")
    used_app = validate_yes_no_input("Did the customer use the app? (Y/N) ")

    break  # Exit the loop if input is valid

# The rest of the program remains the same
PIZZA_PRICE = 12.00
DISCOUNT_TUESDAY = 0.5
DISCOUNT_APP = 0.25
DELIVERY_FEE = 2.50
MIN_DELIVERY_ORDER = 5

total_price = num_pizzas * PIZZA_PRICE

if delivery_required and num_pizzas < MIN_DELIVERY_ORDER:
    total_price += DELIVERY_FEE

discount = 1.0
if is_tuesday:
    discount -= DISCOUNT_TUESDAY
if used_app:
    discount -= DISCOUNT_APP

total_price *= discount

print("\nBPP Pizza Price Calculator")
print("==========================\n")
print(f"How many pizzas ordered? {num_pizzas}")
print(f"Is delivery required? {'Y' if delivery_required else 'N'}")
print(f"Is it Tuesday? {'Y' if is_tuesday else 'N'}")
print(f"Did the customer use the app? {'Y' if used_app else 'N'}\n")
print(f"Total Price: £{total_price:.2f}")
