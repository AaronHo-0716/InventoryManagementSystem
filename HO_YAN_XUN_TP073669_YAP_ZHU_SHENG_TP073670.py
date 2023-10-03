# HO YAN XUN YAP ZHU SHENG
# TP073669   TP073670

import datetime

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

    users = ",".join([userID, userName, "Admin", password])
    
    with open("users.txt", "w") as f:
        f.write(users)

    # supplierCode, supplierName
    # suppliers = [["JJ", "Johnson & Johnson"],["AG", "Agile Ground"], ["EW", "Ewwww"]]
    
    try:
        open("supplier.txt", "r")       
    except FileNotFoundError:
        print("\nInitializing suppliers.txt...")
        while True:
            suppliers = []
            
            try:
                supplierCode = list(input("Please enter the all the supplier code with comma in between: ").strip().split(','))
                supplierName = list(input("Please enter the all the supplier name with comma in between: ").strip().split(','))

                for i in range(0,3):
                    suppliers.append([supplierCode[i], supplierName[i]])
                
                writeToFile("suppliers.txt", sorted(suppliers))
                print("Initializing complete")
                break

            except Exception as e:
                print(e)
                                     
    # hospitals = [["KKM", "Klinik Kesihatan Muhibbah"], ["KKPBJ", "Klinik Komuniti Pinggiran Bukit Jalil"], ["CAH","Columbia Asia Hospital"]]
    
    try:
        open("hospitals.txt", "r")
    except FileNotFoundError:
        while True:
            print("\nInitializing hospitals.txt...")
            hospitals = []
            
            try:
                hospitalCode = list(input("Please enter the all the hospital code with comma in between: ").strip().split(','))
                hospitalName = list(input("Please enter the all the hospital name with comma in between: ").strip().split(','))

                for i in range(0,3):
                    hospitals.append([hospitalCode[i], hospitalName[i]])
                
                writeToFile("hospitals.txt", sorted(hospitals))
                print("Initializing complete")
                break

            except Exception as e:
                print(e)
    print("Initialization complete.")

def readFile(filePath):
    content = []
    with open(filePath, 'r') as f:
        while True:
            line = f.readline().rstrip('\n')
            if not line:
                break
            else:
                content.append(list(line.split(',')))

    return content

def writeToFile(fileName, original):
    with open(fileName, 'w') as f:
        for i in original:
            f.write(','.join(i))
            f.write('\n')

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
        
        original = readFile("users.txt")

        for user in original:
            if user[0] == newUserID:
                print("This userID already exists")
                duplicateUserDetected = True

        if not duplicateUserDetected:
            original.append(users)
            writeToFile('users.txt',original)
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
            users = readFile('users.txt')

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

                writeToFile("users.txt",users)

                print("User deleted\n")
                break
    

def searchUser():
    while True:
        userFound = False
        searchTerm = input("\nSearch user by their user code(Type \"Quit\" to quit):")
        if searchTerm == "Quit":
            break
        
        users = readFile("users.txt")
        for user in users:
            if user[0] == searchTerm:
                print(f"Found user: {user[0]}\nName: {user[1]}\nType: {user[2]}")
                userFound = True

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
            users = readFile('users.txt')

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
                                        writeToFile("users.txt",users)
                                        break
                                    case "Staff":
                                        if mod == 1:
                                            print("This account is the master account, you cannot change the type of it")
                                            continue
                                        else:
                                            users[mod - 1][2] = "Staff"
                                            writeToFile("users.txt",users)
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

                                    writeToFile("users.txt", users)
                                    break

                                else:
                                    print("Old password isn't correct please try again")
                        
                    except Exception as e:
                        print(e)
                        
def listUsers():
    users = readFile("users.txt")
    print(f"{'No.' : <5}{'User ID' : ^15}{'User Name' : ^15}{'User Type' : ^15}")

    for k,v in enumerate(users):
        print(f"{k+1 : <5}{v[0] : ^15}{v[1] : ^15}{v[2] : ^15}")

def mainMenu(loginInfo):
    while True:
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
                
                case 2:
                    listSuppliers()
                case 3:
                    listHospitals()
                case 4:
                    if loginInfo[3] == "Admin":
                        manageUsers(loginInfo)
                    else:
                        print("You are not an admin")
                case 5:
                    print("\n")
                    break

                case _:
                    print("Value entered not a valid choice, pls try again")

def loginMenu():
    users = readFile('users.txt')

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
        while True:
            ppes = []
            
            try:
                ppe = list(input("Please enter the all the item code with comma in between: ").strip().split(','))
                ppeName = list(input("Please enter the all the item name with comma in between: ").strip().split(','))
                ppeSupplier = list(input("Please enter the all the supplier code for each item with comma in between: ").strip().split(','))

                for i in range(0,6):
                    ppes.append([ppe[i], ppeName[i], ppeSupplier[i], "100"])
                    addTranscation(ppe[i], ppeName[i], ppeSupplier[i], "100", "receive")
                
                writeToFile("ppe.txt", sorted(ppes))
                break

            except Exception as e:
                print(e)

def inventory():
    inventoryInit()
    
    while True:
        print("\nInventory")
        print("1. Check Stock")
        print("2. Receive Items")
        print("3. Distribute Items")
        print("4. Transaction History")
        print("5. Search")
        print("6. Quit")
        
        choice = input("Select one: ")
        match choice:
            case "1":
                listStock()
            case "2":
                receiveItems()
            case "3":
                distributeItems()
            case "4":
                history()
            case "5":
                search()
            case "6":
                break
            case _:
                print("Choice entered not valid, pls try again")

def receiveItems():
    ppes = readFile("ppe.txt")
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
                    ppes[k][3] = int(ppes[k][3])
                    ppes[k][3] += int(amount)
                    ppes[k][3] = str(ppes[k][3])
                    
                    writeToFile("ppe.txt", ppes)
                    addTranscation(v[0],v[1],v[2],amount,"receive")
                    break
        except Exception as e:
            print(e)


def doesItemExists(element, li):
    for i in li:
        if i[0] == element:
            return True

    return False


def distributeItems():
    ppes = readFile("ppe.txt")
    hospitals = readFile("hospitals.txt")
    listStock()
    while True:
        choice = input("\nSelect the item distributing(Item Code, Type \"Quit\" to quit):")

        if choice == 'Quit':
            break

        if not doesItemExists(choice, ppes):
            print("Item doesn't exits please try again")
            continue

        while True:
            listHospitals()
            hospitalChoice = input("\nSelect the hospital distributing to(Hospital Code):")

            if not doesItemExists(hospitalChoice, hospitals):
                print("Hospital doesn't exits please try again")
                continue
            
            while True:
                amount = input("Input the amount distributed:")
                
                try:
                    for k,v in enumerate(ppes):
                        if v[0] == choice:
                            ppes[k][3] = int(ppes[k][3])

                            # Check for sufficient quantity
                            if ppes[k][3] - int(amount) >= 0:
                                
                                ppes[k][3] -= int(amount)
                                ppes[k][3] = str(ppes[k][3])

                                writeToFile("ppe.txt", ppes)
                                addTranscation(v[0],v[1],hospitalChoice,amount,"distribute")
                                addDistribution(v[0],v[1],hospitalChoice,amount)
                                
                                break
                            
                            else:
                                print(f"Insufficient amount, current stock left is {ppes[k][3]},  please try again")
                                
                            ppes[k][3] = str(ppes[k][3])

                    break
                except Exception as e:
                    print(e)
            break

def history():
    while True:
        print("\nWelcome to history")
        print("1. Transaction Full History")
        print("2. Distribution History")
        print("3. Transaction Between a Time Period")

        choice = input("\nPlease select one(Type \"Quit\" to quit): ")

        match choice:
            case "Quit":
                break
            
            case "1":
                transactions = readFile("transaction.txt")
                print(f"\n{'Transaction Time' : <30}{'Item Name' : ^20}{'Item Code' : ^20}{'Item Quantity' : ^15}{'Supplier or Hospital Code' : ^40}{'Status' : ^10}")

                for v in transactions:
                    print(f"{v[0] : <30}{v[1] : ^20}{v[2] : ^20}{v[3] : ^15}{v[4] : ^40}{v[5] : ^10}")
            case "2":
                distributions = readFile("distribution.txt")
                print(f"\n{'Distribution Time' : <30}{'Item Name' : ^20}{'Item Code' : ^20}{'Item Quantity' : ^15}{'Hospital Code' : ^40}")

                for v in distributions:
                    print(f"{v[0] : <30}{v[1] : ^20}{v[2] : ^20}{v[3] : ^15}{v[4] : ^40}")

            case "3":
                while True:
                    print("\nSearch for transactions during a time period\n*leave blank for default*")
                    sDate = input("Please input the starting date(dd/mm/yyyy): ")
                    eDate = input("Please input the ending date(dd/mm/yyyy): ")

                    print(sDate,eDate)
                    
                    sDateDT = None
                    eDateDT = None
                    
                    if sDate == '' and eDate == '':
                        sDateDT = datetime.datetime.strptime("01/01/0001", "%d/%m/%Y")
                        eDateDT = datetime.datetime.strptime("31/12/9999", "%d/%m/%Y")

                    elif sDate == '':
                        sDateDT = datetime.datetime.strptime("01/01/0001", "%d/%m/%Y")
                        try:
                            eDateDT = datetime.datetime.strptime(eDate, "%d/%m/%Y")
                        except Exception as e:
                            print(e)
                            continue
                        
                    elif eDate == '':
                        try:
                            sDateDT = datetime.datetime.strptime(sDate, "%d/%m/%Y")
                        except Exception as e:
                            print(e)
                            continue
                        eDateDT = datetime.datetime.strptime("31/12/9999", "%d/%m/%Y")

                    else:
                        try:
                            sDateDT = datetime.datetime.strptime(sDate, "%d/%m/%Y")
                            eDateDT = datetime.datetime.strptime(eDate, "%d/%m/%Y")

                        except Exception as e:
                            print(e)
                
                    if isinstance(sDateDT, datetime.datetime) and isinstance(eDateDT, datetime.datetime):
                        transactionBetweenTimePeriod(sDateDT,eDateDT)
                        break
                    
                    else:
                        print("Either or both the dates are not in correct format please try again")
                        continue

def transactionBetweenTimePeriod(startDate, endDate):
    transactions = readFile("transaction.txt")
    transactionDates = []
    indexOfFilteredDates = []

    for transaction in transactions:
        transactionDates.append(convStrToDT(transaction[0]))

    print(transactionDates)

    for k, date in enumerate(transactionDates):
        if date >= startDate and date <= endDate:
            print(date)
            indexOfFilteredDates.append(k)

    print(indexOfFilteredDates)

def convStrToDT(s):
    date = datetime.datetime.strptime(s, "%Y-%m-%d %H:%M:%S.%f").strftime("%d/%m/%Y")
    return datetime.datetime.strptime(date, "%d/%m/%Y")
    
def addTranscation(itemCode, itemName, supplierOrHospitalCode, quantity, transactionType):
    with open("transaction.txt","a") as f:
        if transactionType == "receive":
            f.write(f'{datetime.datetime.now()},{itemName},{itemCode},{quantity},{supplierOrHospitalCode},received')
        elif transactionType == "distribute":
            f.write(f'{datetime.datetime.now()},{itemName},{itemCode},{quantity},{supplierOrHospitalCode},distributed')
        f.write('\n')
        

def addDistribution(itemCode, itemName, hospitalCode, quantity):
    with open("distribution.txt","a") as f:
        f.write(f'{datetime.datetime.now()},{itemName},{itemCode},{quantity},{hospitalCode}')
        f.write('\n')

def listStock():
    ppe = readFile("ppe.txt")
    print(f"\n{'Item Code' : <10}{'Item Name' : ^20}{'Item Quantity' : ^15}")

    for v in ppe:
        print(f"{v[0] : <10}{v[1] : ^20}{v[3] : ^15}")
            
def listHospitals():
    hospitals = readFile("hospitals.txt")
    print(f"\n{'Hospital Code' : <15}{'Hospital Name' : ^40}")

    for v in hospitals:
        print(f"{v[0] : <15}{v[1] : ^40}")
        
def listSuppliers():
    suppliers = readFile("suppliers.txt")
    print(f"\n{'Supplier Code' : <15}{'Supplier Name' : ^25}")

    for v in suppliers:
        print(f"{v[0] : <15}{v[1] : ^25}")

def main():
    initCheck()
    while True:
        # loginStatus, userID, userName, userType
        loginInfo = loginMenu()

        print(f"\nWelcome {loginInfo[2]}")

        mainMenu(loginInfo)

if __name__ == "__main__":
    main()
