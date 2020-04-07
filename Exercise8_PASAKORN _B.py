IDInput = input("ID   : ")
PASSWORDInput = input("PASS : ")
if IDInput == "admin" and PASSWORDInput == "1111":
    print("-------------------------------------")
    print("lnwzaRi007shop - red/wing/raycard")
    print("-------------------------------------")
    print("Press  1 > Red Potion    1ea  =  30 Z")
    print("Press  2 > Wing          1ea  =  60 Z")
    print("Press  3 > Raydric Card  1ea  =  1  Z")
    print("-------------------------------------")
    usernameSelected = int(input("You Press ?  : "))
    if usernameSelected == 1:
        print("You choose   : Red Potion")
        Red = int(30)
        Ea = int(input("How many ?   : "))
        print("Total        : ",int(Red * Ea), "Zeny")
    elif usernameSelected == 2:
        print("You choose   : Wing")
        Wing = int(60)
        Ea = int(input("How many ?   : "))
        print("Total        : ",int(Wing * Ea), "Zeny")
    elif usernameSelected == 3:
        print("You choose   : Raydric Card")
        print("Sold Out ! ")
else:
    print("Failed Login")