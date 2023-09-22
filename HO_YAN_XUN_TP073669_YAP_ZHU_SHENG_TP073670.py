# HO YAN XUN
# TP073669

# YAP ZHU SHENG
# TP073670

# Check if the program is running the first time
# Checks by detecting the existence of users.txt and other files
def initCheck():
    isFirst = False
    try:
        open('users.txt', "r")
    except FileNotFoundError:
        print("Initializing system...")
        isFirst = True

    if isFirst:
        initialization()

# Creates users.txt and ppe.txt and propmts user to create a admin account and enter the items
def initialization():
    print("Entering initialization, please enter the userID and password for creating an admin account")
    userID = input("Please enter your userID: ")
    password = input("Please enter your password: ")
    
    with open("users.txt", "w") as f:
        f.write("[{\"userID\": \"" + userID + "\", \"userType\": \"Admin\", \"password\": \"" + password + "\"}]")

    ppe = [{"itemCode": "HC", "itemName": "Head Cover", "supplierCode": "JJ", "quantity": 100}, {"itemCode": "FS", "itemName": "Face Shield", "supplierCode": "JJ", "quantity": 100}, {"itemCode": "MS", "itemName": "Mask", "supplierCode": "AG", "quantity": 100}, {"itemCode": "GL", "itemName": "Gloves", "supplierCode": "AG", "quantity": 100}, {"itemCode": "GW", "itemName": "Gown", "supplierCode": "EW", "quantity": 100}, {"itemCode": "SC", "itemName": "Show Covers", "supplierCode": "EW", "quantity": 100}]

    with open("ppe.txt", "w") as f:
        f.write(str(ppe))

    print("Initialization complete.")

def addUser():
    print("User Type")
    print("1. Admin")
    print("2. Staff")
    choice=input("Select one: ")
    match choice:
        case 1:
            userType="admin"
        case 2:
            userType="staff"
    newUser=input("Please enter your userID: ")
    newPwd=input("Please enter your password: ")
    with open("users.txt","w") as f:
        f.write("[{\"userID\": \"" + newUser + "\", \"userType\": \""+ userType + "\", \"password\": \"" + newPwd + "\"}]")
    print("Added New User")


<<<<<<< Updated upstream
def mainMenu():
    choice = input()
=======
def mainMenu(loginInfo):
    print("\nWelcome to the PPE Inventory Management System")
    print("1. Inventory")
    print("2. Suppliers")
    print("3. Hospitals")
    print("4. User Management")
    print("5. Log Out")
    
    choice = input("Select one: ")
>>>>>>> Stashed changes
    try:
        int(choice)
    except:
        print("Value entered not a valid integer, pls try again")
    else:
        match int(choice):
            case 5:
<<<<<<< Updated upstream
                quit()
=======
                print("\n")
                return None
            case _:
                print("Value entered not a valid choice, pls try again")
>>>>>>> Stashed changes

def loginMenu():
    userID = input("Please enter your userID: ")
    password = input("Please enter your password: ")
        
    try:
        with open('users.txt', 'r') as f:
            users = eval(f.read())

            for k,v in enumerate(users):
                if userID == v[0] and password == v[3]:
                    return [True, userID,users[k][1], users[k][2]]
                
    except:
        print("Login error, pls try again \n")
        return [False, None, None, None]
    else:
        print("Wrong userID or password, pls try again\n")
        return [False, None, None, None]

def inventory():
    while True:
        print("\nInventory")
        print("1. Check Stock")
        print("2. Receive Items")
        print("3. Distribute Items")
        print("4. Transaction History")
        print("5. Quit")
        
        choice = input("Select one: ")
        match choice:
            case "1":
                listStock()
            case "2":
                receiveItems()
            case "3":
                distributeItems()
            case "4":
                transactionHistory()
            case "5":
                break
            case _:
                print("Choice entered not valid, pls try again")

def receiveItems():
    pass

def distributeItems():
    pass

def transactionHistory():
    pass

def listStock():
    with open("ppe.txt", "r") as f:
        ppe = eval(f.read())
        print(f"\n{'Item Code' : <10}{'Item Name' : ^20}{'Item Quantity' : ^10}")

        for v in ppe:
<<<<<<< Updated upstream
            print(f"{v[0] : <10}{v[1] : ^20}{v[3] : ^10}")

def main():
    loginInfo = {"loginStatus": False, "userID": None, "userType": None}
    
    initCheck()
    while not loginInfo["loginStatus"]:
        loginInfo = loginMenu()

    print(f"You are logined as {loginInfo['userType']}, your ID is {loginInfo['userID']}")
    
    while True:
        mainMenu()
=======
            print(f"{v[0] : <10}{v[1] : ^20}{v[3] : ^15}")

def main():
    while True:
        # loginStatus, userID, userName, userType
        loginInfo = [False, None, None, None]
        
        initCheck()
        loginInfo = loginMenu()

        print(f"\nWelcome {loginInfo[2]}")

        mainMenu(loginInfo)
>>>>>>> Stashed changes

if __name__ == "__main__":
    main()
