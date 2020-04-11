def Login():
    IDInput = input("ID        ")
    PASSWORDInput = input("PASSWORD  ")
    if IDInput == "admin" and PASSWORDInput == "1111":
        return True
    else:
        return False

def ShowMenu():
    print("Welcom to myShop")
    print("1.Vat Cal")
    print("2.Price Cal")

def SelectMenu():
    usernameSelected = int(input(">>"))
    return usernameSelected

def vatCal(totalPrice):
    vat = 7
    result = totalPrice + (totalPrice * vat / 100)
    return result

def priceCal():
    price1 = int(input("First Product Price : "))
    price2 = int(input("Second Product Price : "))
    return vatCal(price1 + price2)

if Login() == True:
    ShowMenu()
    usernameSelected = SelectMenu()
    if usernameSelected == 1:
        priceInput = int(input("Price (THB) : "))
        print("Total : ",vatCal(priceInput))
    elif usernameSelected  == 2:
        print("Total : ",priceCal())
else:
    print("Failed Login")