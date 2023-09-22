# HO YAN XUN YAP ZHU SHENG
# TP073669   TP073670

# Check if the program is running the first time
# Checks by detecting the existence of users.txt and other files
def initCheck():
    try:
        open('users.txt', "r")
    except FileNotFoundError:
        print("Initializing system...")
        initialization()

# Creates users.txt and ppe.txt and propmts user to create a admin account and enter the items
def initialization():
    print("\nEntering initialization, please enter the userID and password for creating an admin account")
    userID = input("Please enter your userID: ")
    userName = input("Please enter your name: ")
    password = input("Please enter your password: ")

    users = ','.join([userID, userName, "Admin", password])
    
    with open("users.txt", "w") as f:
        f.write(users)

    # supplierCode, supplierName
    suppliers = [["JJ", "Johnson & Johnson"],["AG", "Agile Ground"], ["EW", "Ewwww"]]
    
    with open("suppliers.txt", "w") as f:
        f.write(str(suppliers))

    hospitals = [["KKM", "Klinik Kesihatan Muhibbah"], ["KKPBJ", "Klinik Komuniti Pinggiran Bukit Jalil"], ["CAH","Columbia Asia Hospital"]]
    
    with open("hospitals.txt", "w") as f:
        f.write(str(hospitals))

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
        print("\nSelect the user you want to delete(Type \"Quit\" to quit): ")
        listUsers()
        
        delete = input()
        
        if delete == "Quit":
            break
        
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
                if users[int(delete)  - 1][0] == loginInfo[1]:
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
        print("\nSelect the user you want to modify(Type \"Quit\" to quit):")
        listUsers()

        mod = input()
        
        if mod == "Quit":
            break

        try:
            mod = int(mod)
        except:
            print("Value entered is not a valid integer, pls try again")
        else:
            users = None

            with open("users.txt", "r+") as f:
                users = eval(f.read())

            try:
                users[mod  - 1][0] 
            except IndexError:
                print("User doesn't exitst")

            else:
                while True:
                    print("\nSelect the action to perform(Type \"Quit\" to quit):")
                    print("1. Change user type")
                    print("2. Change password")

                    choice = input()

                    try:
                        if choice == "Quit":
                            break
                        elif choice == "1":
                            while True:
                                print("\nSelect one(Admin, Staff ; Type \"Quit\" to quit):")
                                changeType = input()
                                match changeType:
                                    case "Admin":
                                        users[mod - 1][2] = "Admin"
                                        with open("users.txt", "w") as f:
                                            f.write(str(users))
                                        break
                                    case "Staff":
                                        if mod == 1:
                                            print("This account is the master account, you cannot change the type of it")
                                            continue
                                        else:
                                            users[mod - 1][2] = "Staff"

                                            with open("users.txt", "w") as f:
                                                f.write(str(users))
                                            break
                                    case "Quit":
                                        break
                                    case _:
                                        print("Error, please enter only \"Admin\" or \"Staff\"")
                        elif choice == "2":
                            while True:
                                oldPass = input("\nType the old password:")
                                newPass = input("Type the new password:")

                                if oldPass == users[mod - 1][3]:
                                    users[mod - 1][3] = newPass

                                    with open("users.txt", "w") as f:
                                        f.write(str(users))
                                    break

                                else:
                                    print("Old password isn't correct please try again")
                        
                    except Exception as e:
                        print(e)
                        
def listUsers():
    with open("users.txt", "r") as f:
        users = eval(f.read())
        print(f"{'No.' : <5}{'User ID' : ^15}{'User Name' : ^15}{'User Type' : ^15}")

        for k,v in enumerate(users):
            print(f"{k+1 : <5}{v[0] : ^15}{v[1] : ^15}{v[2] : ^15}")

def mainMenu(loginInfo):
    print("\nWelcome to the PPE Inventory Management System")
    print("1. Inventory")
    print("2. Suppliers")
    print("3. Hospitals")
    print("4. User Management")
    print("5. Log Out")
    
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
                print("\n")
                return None

            case _:
                print("Value entered not a valid choice, pls try again")

def loginMenu():
    with open('users.txt','r') as f:
        users = eval(f.read())

    while True:
        print("Welcome to PPE Inventory Management System")      
        print("Type \"quit\" to quit the program\n")      
        userID = input("Please enter your userID: ")
        for k,v in enumerate(users):
            if userID == v[0]:
                while True:
                    password = input("Please enter your password: ")
                    if password == v[3]:
                        return [True, userID,users[k][1], users[k][2]]
                    else:
                        print("Wrong password, pls try again\n")
            elif userID == "quit":
                quit()
        print("User doesn't exist, pls try again.\n")

def inventoryInit():
    try:
        open("ppe.txt", "r")       
    except FileNotFoundError:
        ppes = []
        
        with open("ppe.txt", "w") as f:
            ppe = list(input("Please enter the all the item code with comma in between: ").strip().split(','))
            ppeName = list(input("Please enter the all the item name with comma in between: ").strip().split(','))
            ppeSupplier = list(input("Please enter the all the supplier code for each item with comma in between: ").strip().split(','))

            for i in range(0,6):
                ppes.append([ppe[i], ppeName[i], ppeSupplier[i], 100])
            
            f.writelines(sorted(ppes))

def inventory():
    inventoryInit()
    
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
    with open("ppe.txt", "r+") as f:
        ppes = eval(f.read())
        listStock()
        while True:
            choice = input("\nSelect the item receiving(Item Code, Type \"Quit\" to quit):")

            if choice == 'Quit':
                break

            if not doesItemExists(choice, ppes):
                print("Item doesn't exits please try again")
                continue

            amount = input("Input the amount received:")

            try:
                for k,v in enumerate(ppes):
                    if v[0] == choice:
                        ppes[k][3] += int(amount)
                        f.seek(0)
                        f.truncate()
                        f.write(str(ppes))
                        print(ppes)
            except Exception as e:
                print(e)


def doesItemExists(element, li):
    for i in li:
        if i[0] == element:
            return True

    return False


def distributeItems():
    with open("ppe.txt", "r+") as f:
        ppes = eval(f.read())
        listStock()
        while True:
            choice = input("\nSelect the item distributing(Item Code, Type \"Quit\" to quit):")

            if choice == 'Quit':
                break

            if not doesItemExists(choice, ppes):
                print("Item doesn't exits please try again")
                continue

            while True:
                amount = input("Input the amount distributed:")
                

                try:
                    for k,v in enumerate(ppes):
                        if v[0] == choice:
                            ppes[k][3] += int(amount)
                            f.seek(0)
                            f.truncate()
                            f.write(str(ppes))
                            print(ppes)
                except Exception as e:
                    print(e)

def transactionHistory():
    pass

def listStock():
    with open("ppe.txt", "r") as f:
        ppe = eval(f.read())
        print(f"\n{'Item Code' : <10}{'Item Name' : ^20}{'Item Quantity' : ^15}")

        for v in ppe:

            print(f"{v[0] : <10}{v[1] : ^20}{v[3] : ^15}")
            
def main():
    while True:
        # loginStatus, userID, userName, userType
        loginInfo = [False, None, None, None]
        
        initCheck()
        loginInfo = loginMenu()

        print(f"\nWelcome {loginInfo[2]}")

        mainMenu(loginInfo)

if __name__ == "__main__":
    main()
