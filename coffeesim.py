import time
import os

print("Bean There, Done That Coffee")
receipt_path = 'reciept.py'

def item1():
   item1 = "Latte"
   item1_price = int(3.00)
   item1_price_print = (f"${item1_price}")
   item1_full = (item1 + " " + item1_price_print)
   return item1_full

def item2():
   item2 = "Cappucino"
   item2_price = int(5.00)
   item2_price_print = (f"${item2_price}")
   item2_full = (item2 + " " + item2_price_print)
   return item2_full

def item3():
   item3 = "Mocha Frap."
   item3_price = int(7.00)
   item3_price_print = (f"${item3_price}")
   item3_full = (item3 + " " + item3_price_print)
   return item3_full

def item4():
   item4 = "Brownie"
   item4_price = int(3.00)
   item4_price_print = (f"${item4_price}")
   item4_full = (item4 + " " + item4_price_print)
   return item4_full

def item5():
   item5 = "Cookie"
   item5_price = int(3.00)
   item5_price_print = (f"${item5_price}")
   item5_full = (item5 + " " + item5_price_print)
   return item5_full


def display_menu(state):    
    print("Menu:")
    print("Drinks")
    print(item1()) 
    print(item2())
    print(item3())
    print("Bakery")
    print(item4())
    print(item5())
    state = "working"
    return state

def take_order(item1_price, item2_price, item3_price, item4_price, item5_price):
   add_to_bag = input("Type item name to add to bag: ")
   if add_to_bag == "Latte":
      with open(receipt_path, 'a') as receipt:
        receipt.write(f"Latte {item1_price} \n")
   
   if add_to_bag == "Cappucino":
      with open(receipt_path, 'a') as receipt:
        receipt.write(f"Cappucino {item2_price} \n")

   if add_to_bag == "Mocha Frap.":
      with open(receipt_path, 'a') as receipt:
        receipt.write(f"Mocha Frap. {item3_price} \n")

   if add_to_bag == "Brownie":
        with open(receipt_path, 'a') as receipt:
            receipt.write(f"Brownie {item4_price} \n")

   if add_to_bag == "Cookie":
        with open(receipt_path, 'a') as receipt:
            receipt.write(f"Cookie {item5_price} \n")

   if add_to_bag == "Done":
      state = "done"
      return state

def receipt_total():
   exit()

# Start of program
time.sleep(1)
state = "idle"
item1_price = int(3.00)
item2_price = int(5.00)
item3_price = int(7.00)
item4_price = int(3.00)
item5_price = int(3.00)

while display_menu(state) == "working":
    take_order(item1_price, item2_price, item3_price, item4_price, item5_price)

while state == "done":
    receipt_total()
    


