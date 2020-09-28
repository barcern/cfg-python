# Your boss really likes calculating VAT on their purchases.
# They've written this code to calculate VAT. Fix it.

# We are missing a return statement
def calculate_vat(amount):
    with_vat = amount*1.2
    return with_vat

total = calculate_vat(100)
print(total)