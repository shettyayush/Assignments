list1 = ["Laptop", "Mouse", "Keyboard"]
list1.append("Monitor")

new_products = ["Tablets", "Webcam"]
list1.extend(new_products)

list1.remove("Mouse")

shipped = list1.pop()

count_laptops = list1.count("Laptop")

position = list1.index("Monitor")

list1.sort()
list1.reverse()
copy_list = list1.copy()

temp = [1,2]
temp.clear()

print("Final Inventory List:", list1)
print("Shipped Item:", shipped)
print("Count of Laptops:", count_laptops)
print("Position of Monitor:", position)
print("Copied List:", copy_list)
print("Temp List:", temp)
