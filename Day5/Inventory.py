inventory = []

categories = int(input("Enter the number of categories: "))

for i in range(categories):
    category = input("Enter the category name:")
    products = []
    n = int(input("Enter the number of products in this category: "))
    for j in range(n):
        product_name = input("Enter the product name:")
        product_quantity = int(input("Enter the quantity of the product:"))
        products.append([product_name, product_quantity])
    inventory.append([category, products])

print("----Inventory Report: ----")
for category, products in inventory:
    print("Category:", category)
    for product_name, product_quantity in products:
        print(product_name, "Quantity:", product_quantity)