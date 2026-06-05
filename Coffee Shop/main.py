import time
import os
import reciept

print("Bean There, Done That Coffee")
receipt_path = 'Coffee Shop/reciept.py'

def item1func(item1):
   item1 = "Latte"
   item1_price = int(3.00)
   item1_price_print = (f"${item1_price}")
   item1_full = (item1 + " " + item1_price_print)
   return item1_full, item1

def item2func(item2):
   item2 = "Cappucino"
   item2_price = int(5.00)
   item2_price_print = (f"${item2_price}")
   item2_full = (item2 + " " + item2_price_print)
   return item2_full, item2

def item3func(item3):
   item3 = "Mocha Frap."
   item3_price = int(7.00)
   item3_price_print = (f"${item3_price}")
   item3_full = (item3 + " " + item3_price_print)
   return item3_full, item3

def item4func(item4):
   item4 = "Brownie"
   item4_price = int(3.00)
   item4_price_print = (f"${item4_price}")
   item4_full = (item4 + " " + item4_price_print)
   return item4_full, item4

def item5func(item5):
   item5 = "Cookie"
   item5_price = int(3.00)
   item5_price_print = (f"${item5_price}")
   item5_full = (item5 + " " + item5_price_print)
   return item5_full, item5


def display_menu(item1, item2, item3, item4, item5, item1_price, item2_price, item3_price, item4_price, item5_price):    
    print("Menu:")
    print("Drinks")
    print(item1,item1_price) 
    print(item2,item2_price)
    print(item3,item3_price)
    print("Bakery")
    print(item4,item4_price)
    print(item5,item5_price)
    
    take_order(item1, item2, item3, item4, item5, item1_price, item2_price, item3_price, item4_price, item5_price, receipt_path)

def take_order(item1, item2, item3, item4, item5, item1_price, item2_price, item3_price, item4_price, item5_price, receipt_path):
   
   item_1_order = input("Type first item name to add to bag: ")
   with open(receipt_path, 'w') as reciept_edit:
    if item_1_order == item1 or item2 or item3 or item4 or item5:
            reciept_edit.write(print(item_1_order)) 
            reciept_edit.write(print(" "))
            reciept_edit.write(print(str(item1_price)))
            reciept_edit.write(print('\n'))
    else:
            receipt_total()
   
   item_2_order = input("Type second item name to add to bag: ")
   with open(receipt_path, 'a') as reciept_edit:
    if item_2_order == item1 or item2 or item3 or item4 or item5:
            reciept_edit.write(print(item_2_order))
            reciept_edit.write(print(" "))
            reciept_edit.write(print(str(item2_price)))
            reciept_edit.write(print('\n'))
    else:
            receipt_total()

   item_3_order = input("Type third item name to add to bag: ")
   with open(receipt_path, 'a') as reciept_edit:
    if item_3_order == item1 or item2 or item3 or item4 or item5:
            reciept_edit.write(print(item_3_order)) 
            reciept_edit.write(print(" "))
            reciept_edit.write(print(str(item3_price)))
            reciept_edit.write(print('\n'))
    else:
            receipt_total()

   item_4_order = input("Type fourth item name to add to bag: ")
   with open(receipt_path, 'a') as reciept_edit:
    if item_4_order == item1 or item2 or item3 or item4 or item5:
           reciept_edit.write(print(item_4_order)) 
           reciept_edit.write(print(" "))
           reciept_edit.write(print(str(item4_price)))
           reciept_edit.write(print('\n'))
    else:
            receipt_total()

   item_5_order = input("Type fifth item name to add to bag: ")
   with open(receipt_path, 'a') as reciept_edit:
    if item_5_order == item1 or item2 or item3 or item4 or item5:
            reciept_edit.write(print(item_5_order)) 
            reciept_edit.write(print(" "))
            reciept_edit.write(print(str(item5_price)))
            reciept_edit.write(print('\n'))
    else:
            receipt_total()

   
def receipt_total():
   os.system('clear')
   exit()

# Start of program
time.sleep(1)
item1_price = int(3.00)
item2_price = int(5.00)
item3_price = int(7.00)
item4_price = int(3.00)
item5_price = int(3.00)
item1 = "Latte"
item2 = "Cappucino"
item3 = "Mocha Frap."
item4 = "Brownie" 
item5 = "Cookie"

display_menu(item1, item2, item3, item4, item5, item1_price, item2_price, item3_price, item4_price, item5_price)
