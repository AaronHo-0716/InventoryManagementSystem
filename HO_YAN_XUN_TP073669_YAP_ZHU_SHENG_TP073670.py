# HO YAN XUN YAP ZHU SHENG
# TP073669   TP073670

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
    print("\nEntering initialization, please enter the userID and password for creating an admin account")
    userID = input("Please enter your userID: ")
    userName = input("Please enter your name: ")
    password = input("Please enter your password: ")

    users = [[userID, userName, "Admin", password]]
    
    with open("users.txt", "w") as f:
        f.write(str(users))

    # itemCode, itenName, supplierCode, quantity
    ppe = [["HC","Head Cover", "JJ", 100], ["FS","Face Shield", "JJ", 100], ["MS","Mask", "AG", 100], ["GL","GLoves", "AG", 100], ["GW","Gown", "EW", 100], ["SC","Shoe Covers", "EW", 100]]

    with open("ppe.txt", "w") as f:
        f.write(str(ppe))

    # supplierCode, supplierName
    suppliers = [["JJ", "Johnson & Johnson"],["AG", "Agile Ground"], ["EW", "Ewwww"]]
    
    with open("suppliers.txt", "w") as f:
        f.write(str(suppliers))

    print("Initialization complete.")

def manageUsers(loginInfo):
    while True:
        print("\nWelcome to Admin panel")
        print("1. Add New User")
        print("2. Delete User")
        print("3. Search User")
        print("4. Modify User")
        print("5. Quit")
        
        choice = input("Select one: ")
        match choice:
            case "1":
                addUser()
            case "2":
                delUser(loginInfo)
            case "3":
                searchUser()
            case "4":
                modifyUser()
            case "5":
                break
            case "6":
                listUsers()
            case _:
                print("Choice entered not valid, pls try again")
    

def addUser():
    
    userType = None
    
    while True:
        print("\nUser Type")
        print("1. Admin")
        print("2. Staff")
        print("3. Quit")
        choice = input("Select one: ")
        match choice:
            case "1":
                userType = "Admin"
                break
            case "2":
                userType = "Staff"
                break
            case "3":
                break
            case _:
                print("Choice entered not valid, pls try again")
            
    while True:
        newUserID = input("Please enter your userID: ")
        newName = input("Please enter your name: ")
        newPwd = input("Please enter your password: ")
        
        users = [newUserID, newName, userType, newPwd]
        original = None
        duplicateUserDetected = False
        
        f = open("users.txt","r+")
        original = eval(f.read())

        for user in original:
            if user[0] == newUserID:
                print("This userID already exists")
                duplicateUserDetected = True

        if not duplicateUserDetected:
            original.append(users)
            f.seek(0)
            f.truncate()
            f.write(str(original))
            print("Added New User")
            break

def delUser(loginInfo):
    while True:
        print("\nSelect the user you want to delete(Type 0 to quit): ")
        
        listUsers()
        
        delete = input()
        try:
            int(delete)
        except:
            print("Value entered is not a valid integer, pls try again")
        else:
            users = None

            with open("users.txt", "r") as f:
                users = eval(f.read())

            try:
                users[int(delete)  - 1][0] 
            except IndexError:
                print("User doesn't exitst")

            else:
                if delete == "0":
                    break
                elif users[int(delete)  - 1][0] == loginInfo[1]:
                    print("You cannot delete yourself")
                    continue
                else:
                    users.pop(int(delete) - 1)

                with open("users.txt", "w") as f:
                    f.write(str(users))

                print("User deleted\n")
                break
    

def searchUser():
    while True:
        userFound = False
        searchTerm = input("\nSearch user by their user code(Type \"Quit\" to quit):")
        if searchTerm == "Quit":
            break
        with open("users.txt", "r") as f:
            users = eval(f.read())
            for user in users:
                if user[0] == searchTerm:
                    print(f"Found user: {user[0]}\nName: {user[1]}\nType: {user[2]}")
                    userFound = True
                    break

        if not userFound:
            print(f"User code {searchTerm} not found")

def modifyUser():
    while True:
        print("\nSelect the user you want to modify(Type 0 to quit):")
        listUsers()

        mod = input()

        try:
            int(mod)
        except:
            print("Value entered is not a valid integer, pls try again")
        else:
            users = None

            with open("users.txt", "r+") as f:
                users = eval(f.read())

            try:
                users[int(mod)  - 1][0] 
            except IndexError:
                print("User doesn't exitst")

            else:
                if mod == "0":
                    break

                while True:
                    print("\nSelect the action to perform(Type 0 to quit):")
                    print("1. Change user type")
                    print("2. Change password")

                    choice = input()

                    try:
                        int(choice)
                    except:
                        print("Value entered is not a valid integer, pls try again")
                    else:
                        if choice == "0":
                            break
                        elif choice == "1":
                            while True:
                                print("\nSelect one(Admin, Staff):")
                                changeType = input()
                                match changeType:
                                    case "Admin":
                                        users[int(mod) - 1][2] = "Admin"
                                        with open("users.txt", "w") as f:
                                            f.write(str(users))
                                        break
                                    case "Staff":
                                        if mod == "1":
                                            print("This account is the master account, you cannot change the type of it")
                                            continue
                                        else:
                                            users[int(mod) - 1][2] = "Staff"

                                            with open("users.txt", "w") as f:
                                                f.write(str(users))
                                            break
                                    case _:
                                        print("Error, please enter only \"Admin\" or \"Staff\"")
                        elif choice == "2":
                            while True:
                                oldPass = input("\nType the old password:")
                                newPass = input("Type the new password:")

                                if oldPass == users[int(mod) - 1][3]:
                                    users[int(mod) - 1][3] = newPass

                                    with open("users.txt", "w") as f:
                                        f.write(str(users))
                                    break

                                else:
                                    print("Old password isn't correct please try again")
                        
def listUsers():
    with open("users.txt", "r") as f:
        users = eval(f.read())
        print(f"{'No.' : <5}{'User ID' : ^15}{'User Name' : ^15}{'User Type' : ^15}")

        for k,v in enumerate(users):
            print(f"{k+1 : <5}{v[0] : ^15}{v[1] : ^15}{v[2] : ^15}")


def mainMenu(loginInfo):
    print("\nWelcome to the PPE Inventory Management System")
    print("1. Inventory")
    print("4. User Management")
    print("5. Quit")
    
    choice = input("Select one: ")
    try:
        int(choice)
    except:
        print("Value entered not a valid integer, pls try again")
    else:
        match int(choice):
            case 1:
                inventory()
            case 4:
                if loginInfo[3] == "Admin":
                    manageUsers(loginInfo)
                else:
                    print("You are not an admin")
            case 5:
                quit()
            case _:
                print("Value entered not a valid choice, pls try again")

def loginMenu():
    with open('users.txt','r') as f:
        users = eval(f.read())

    while True:            
        userID = input("Please enter your userID: ")
        for k,v in enumerate(users):
            if userID == v[0]:
                while True:
                    password = input("Please enter your password: ")
                    if password == v[3]:
                        return [True, userID,users[k][1], users[k][2]]
                    else:
                        print("Wrong password, pls try again\n")
        print("User doesn't exist, pls try again.\n")

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
    listStock()
    while True:
        print("\nSelect the item receiving(Item Code):")
        choice = input()

        match choice:
            case 'HC':
                pass
            case 'FS':
                pass
            case 'MS':
                pass
            case 'GL':
                pass
            case 'GW':
                pass
            case 'SC':
                pass
            case _:
                print("Choice entered is not valid")

def distributeItems():
    pass

def transactionHistory():
    pass

def listStock():
    with open("ppe.txt", "r") as f:
        ppe = eval(f.read())
        print(f"\n{'Item Code' : <10}{'Item Name' : ^20}{'Item Quantity' : ^10}")

        for v in ppe:
            print(f"{v[0] : <10}{v[1] : ^20}{v[3] : ^10}")

def main():
    # loginStatus, userID, userName, userType
    loginInfo = [False, None, None, None]
    
    initCheck()
    while not loginInfo[0]:
        loginInfo = loginMenu()

    print(f"\nWelcome {loginInfo[2]}")
    
    while loginInfo[0]:
        mainMenu(loginInfo)

if __name__ == "__main__":
    main()
