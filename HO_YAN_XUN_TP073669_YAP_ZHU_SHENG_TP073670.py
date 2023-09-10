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
    password = input("Please enter your password: ")

    users = [[userID, "Admin", password]]
    
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
        newPwd = input("Please enter your password: ")
        
        users = [newUserID, userType, newPwd]
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
        print("\nSelect the user you want to delete: (type 0 to quit)")
        
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
    pass

def modifyUser():
    pass

def listUsers():
    with open("users.txt", "r") as f:
        users = eval(f.read())
        print("No.\tUser ID\tUser Type")

        for k,v in enumerate(users):
            print(f"{k+1}.\t{v[0]}\t{v[1]}")

def mainMenu(loginInfo):
    print("\nWelcome to the PPE Inventory Management System")
    # print("1. Inventory Update")
    # print("2. Transactions History")
    print("4. User Management")
    print("5. Quit")
    
    choice = input("Select one:")
    try:
        int(choice)
    except:
        print("Value entered not a valid integer, pls try again")
    else:
        match int(choice):
            case 4:
                if loginInfo[2] == "Admin":
                    manageUsers(loginInfo)
                else:
                    print("You are not an admin")
            case 5:
                quit()
            case _:
                print("Value entered not a valid choice, pls try again")

def loginMenu():
    userID = input("Please enter your userID: ")
    password = input("Please enter your password: ")
        
    try:
        with open('users.txt', 'r') as f:
            users = eval(f.read())

            for k,v in enumerate(users):
                if userID == v[0] and password == v[2]:
                    return [True, userID, users[k][1]]
                
    except:
        print("Login error, pls try again \n")
        return [False, None, None]
    else:
        print("Wrong userID or password, pls try again\n")
        return [False, None, None]


def main():
    #       loginStatus, userID, userType
    loginInfo = [False, None, None]
    
    initCheck()
    while not loginInfo[0]:
        loginInfo = loginMenu()

    print(f"\nYou are logined as {loginInfo[2]}, your ID is {loginInfo[1]}")
    
    while True:
        mainMenu(loginInfo)

if __name__ == "__main__":
    main()
