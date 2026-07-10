store = 3
days = 7

for store in range(1, store + 1):
    print("Store :", store)
    total_sales = 0
    for day in range(1, days + 1):
        sales = float(input("Day: " + str(day) + " Sales: "))
        total_sales += sales
    print ("Total sales for store", store, "is:", total_sales)

