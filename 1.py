# DECLARATION OF SIZES AND PRICES OF PRODUCTS
# 1st size = 12oz Hot, 2nd size = 16oz Cold, 3rd size = 20oz Cold
#=== DITO EDIT KUYS ===
threeSize= ["Americano","Cafe Mocha","Cafe Latte","Caramel Macchiato","Salted Caramel Macchiato","White Chocolate Mocha","Spanish Latte","French Vanilla Latte","Caramel Latte",
    "Vanilla Latte","Brown Sugar Espresso","Six Four Five Latte","Sea Salt Latte","Dirty Matcha","Matcha Latte","Vanilla Milk","Chocolate Milk","White Chocolate Matcha",
    "Chamomile Tea"]
threeSizesPrice=[[100, 105, 120],[120, 135, 150],[105, 115, 130],[120, 140, 155],[120, 140, 160],[120, 135, 150],
[115, 130, 145],[120, 135, 150],[120, 140, 160],[115, 130, 145],[115, 130, 145],[130, 145, 160],[130, 145, 160],
[140, 155, 170],[120, 145, 160],[110, 120, 130],[110, 120, 130],[140, 155, 170],[80, 90, 100]]     
twoSize=[ 
    "White Americano","Iced Americano","Strawberry White Chocolate","Mocha","Caramel",
    "Salted Caramel","Coffee Jelly","White Chocolate Mocha","Matcha","Strawberry","Java Chips",
    "Cookies and Cream","Peppermint Mocha","Strawberyy Matcha","Strawberry Black Tea","Lychiee Soda",
    "Blueberry Soda","Green Apple Soda"]
twoSizePrice=[
    [160, 175],[120, 130],[135, 145],[150, 165],[150, 165], [155, 165],[165, 175],[150, 165],
    [120, 135],[165, 176],[170, 185],[185, 200],[165, 180],[90, 100],[90, 100],[90, 100],[90, 100]]
regularSize=[
    "Cheesy Eggdesal","Classic Burger","Cheesy Burger","645 Burger","Classic Tuna","645 Tuna Sandwich","Plain Fries","Flavored Fries","Chocolate Chip Cookie","Smore's Cookie","Chocolate Crinkles"]
regularSizePrice=[
    [50],[50],[60],[75],[75],[105],[50],[70],[35],[50],[15]]
product_prices = []
menu = "" 
menu_price = []
menu_list = []
orderAmount=[]
# para nasa isang container lang lahat ng items
menu_list += threeSize + twoSize + regularSize
# para nasa isang container lang lahat ng prices
menu_price += threeSizesPrice + twoSizePrice + regularSizePrice
stock = [50] * len(menu_list)
orderNum = 0


# Code para naka lista yung Three -> Two -> Regular Size
for i in range(len(menu_list)):
    
    menu += (f"{i + 1}.{menu_list[i]} ")
    orderNum += 1
    if orderNum <= 18:
        print(f"{i + 1}.{threeSize[i]}: {threeSizesPrice[i]}")
    if orderNum >= 19 and orderNum < 30:
        print(f"{i+1}.{twoSize[i - 19]}: {twoSizePrice[i - 19]}")
    if orderNum >= 30:
        print(f"{i+1}.{regularSize[i - 38]}: {regularSizePrice[i - 38]}")


# Ordering natin mga beh
isOrdering = True
orderList = []
newOrder = "y"
# Order loop to beh
while isOrdering:
    orderInput = (input("enter your order: "))
    # check ni orderinput beh kung nasa loob sha ng regularsize 
    if orderInput in regularSize:
        orderAmount=int(input("Amount:"))
        index = menu_list.index(orderInput)
        orderSize = 1
        if orderAmount <= 0:
            print("Enter a valid amount.")
            continue
        if orderAmount > stock[index]:
            print(f"Not enough stock. {menu_list[index]} has {stock[index]} left.")
            continue
        orderList.append([index, orderSize, orderAmount])
        stock[index] -= orderAmount
        print("Added Order!")
        print("------------")
        newOrder = input("Do you want to add another order? (y): ").lower()
    # ganto rin sa twosize
    elif orderInput in twoSize:
        orderAmount=int(input("Amount:"))
        index = menu_list.index(orderInput)
        orderSize = int(input("enter your size:(1,2): "))
        if orderAmount <= 0:
            print("Enter a valid amount.")
            continue
        if orderSize >= 1 and orderSize < 3:
            if orderAmount > stock[index]:
                print(f"Not enough stock. {menu_list[index]} has {stock[index]} left.")
                continue
            orderList.append([index, orderSize, orderAmount])
            stock[index] -= orderAmount
            print("Added Order!")
            print("------------")
            newOrder = input("Do you want to add another order? (y/n): ").lower()
        else:
            print("Invalid size. Please enter a size between 1 and 2.")
    # and threesize beh
    elif orderInput in threeSize:
        orderAmount=int(input("Amount:"))
        index = menu_list.index(orderInput)       
        orderSize = int(input("enter your size:(1,2,3): "))
        if orderAmount <= 0:
            print("Enter a valid amount.")
            continue
        if orderSize >= 1 and orderSize < 4:
            if orderAmount > stock[index]:
                print(f"Not enough stock. {menu_list[index]} has {stock[index]} left.")
                continue
            orderList.append([index, orderSize, orderAmount])
            stock[index] -= orderAmount
            print("Added Order!")
            print("------------")
            newOrder = input("Do you want to add another order? (y/n): ").lower()
    #Error handling beh kung mali ung size na pinasok
        else:
            print("Invalid size. Please enter a size between 1 and 3.")    
    else:
        print("Item not found in the menu.")
    if newOrder != "y":
        break


print("Order Finished")
print("================")
# printing to beh
# orderList = [OrderName : OrderPrice, OrderAmount]
totalPrice = 0

for index, size, quantity in orderList:
    unit_price = menu_price[index][size - 1]
    print(menu_list[index], ":", unit_price, "*", quantity, "=", unit_price*quantity)
    totalPrice += unit_price * quantity

print("----------------")
print(f"Total: {totalPrice}")
print("Thank you for ordering at 654 Cafe!")
print("")
print("")
print("")
print("================")
checkStock = input("Check Stock?: ").lower
print("1. yes")
print("2. no")
if checkStock == "yes":
    print("Remaining stock:")
    # Enumerate the remaining Stock
    for index, item in enumerate(menu_list):
        print({item},":", {stock[index]})
    # arigathanks <3
