import time


print("Grocery Budget Calculator")
budget = (int (input("Enter Total Grocery Budget")))

grocery_items = [] 
item_1_name = grocery_items.append (input ("Name of item 1"))

grocery_prices = []
item_1_price = grocery_prices.append (int (input("price of item 1")))

item_2_name = grocery_items.append (input ("Name of item 2"))
item_2_price = grocery_prices.append (int (input("price of item 2")))

item_3_name = grocery_items.append (input ("Name of item 3"))
item_3_price = grocery_prices.append (int (input("price of item 3")))

item_4_name = grocery_items.append (input ("Name of item 4"))
item_4_price = grocery_prices.append (int (input("price of item 4")))

item_5_name = grocery_items.append (input ("Name of item 5"))
item_5_price = grocery_prices.append (int (input("price of item 5")))

grocery_total = sum (grocery_prices)
budget_final = (budget - grocery_total)

print("Reciept")

for i in range(0, 5):
    grocery_prices[i]
    grocery_items[i]
    print (grocery_items[i], grocery_prices[i])

time.sleep(2)
print("-----------")

print (grocery_total)


print ("leftover amount"), print (budget_final)

if budget_final < budget:
    print("OVER BUDGET :(")
elif budget > budget_final: 
    print("Within Budget!")