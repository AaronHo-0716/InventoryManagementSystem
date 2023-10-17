# HO YAN XUN, YAP ZHU SHENG
# TP073669, TP073670

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
    while True:
        userID = input("Please enter your userID: ")
        userName = input("Please enter your name: ")
        password = input("Please enter your password: ")

        if userID == "" or userName == "" or password == "":
            print("Please fill in all the details\n")
            continue

        break

    users = ",".join([userID, userName, "Admin", password])
    
    with open("users.txt", "w") as f:
        f.write(users)
    supplierInitialize()
    hospitalInitialize()
    print("Initialization complete.\n")
    # supplierCode, supplierName
    
def supplierInitialize():
    # suppliers = [["JJ", "Johnson & Johnson"],["AG", "Agile Ground"], ["EW", "Ewwww"]]  
    try:
        open("suppliers.txt", "r")        
    except FileNotFoundError:
        print("\nInitializing suppliers.txt...\n")
        while True:
            suppliers = []
            try:
                while True:
                    supplierAmount = input("Do you have 3 or 4 suppliers: ")
                    match supplierAmount:
                        case "3":
                            break
                        case "4":
                            break
                        case _:
                            print("\nPlease enter 3 or 4 only.\n")
                            continue
                while True:
                    print("\nPlease enter the details of "+str(supplierAmount)+ " suppliers only.")
                    print("Example: AA,BB,CC\n")
                    supplierCode = list(input("Please enter the all the supplier code with comma in between: ").strip().split(','))
                    supplierName = list(input("Please enter the all the supplier name with comma in between: ").strip().split(','))
                    supplierContact = list(input("Please enter the all the supplier contact number with comma in between: ").strip().split(','))

                    if supplierCode =="" or supplierName == "" or supplierContact == "":
                        continue
                    else:
                        break

                for i in range(0,int(supplierAmount)):
                    suppliers.append([supplierCode[i], supplierName[i], supplierContact[i]])
                
                writeToFile("suppliers.txt", sorted(suppliers))
                print("Initializing complete")
                break
            
            except IndexError:
                print("\nError in input, please try again.\n")

            except Exception as e:
                print(e)

    return

def  hospitalInitialize():
    try:
        open("hospitals.txt","r")
    except FileNotFoundError:
        print("\nInitializing system...\n")
    # hospitals = [["KKM", "Klinik Kesihatan Muhibbah"], ["KKPBJ", "Klinik Komuniti Pinggiran Bukit Jalil"], ["CAH","Columbia Asia Hospital"]]
        while True:
            hospitals = []
            while True:
                hospitalAmount = input("Do you have 3 or 4 hospitals: ")
                match hospitalAmount:
                    case "3":
                        break
                    case "4":
                        break
                    case _:
                        print("\nPlease enter 3 or 4 hospitals only.\n")
                        continue
            try:
                print("\nPlease enter the details of "+str(hospitalAmount)+" hospitals only.")
                print("Example: AA,BB,CC\n")
                hospitalCode = list(input("Please enter the all the hospital code with comma in between: ").strip().split(','))
                hospitalName = list(input("Please enter the all the hospital name with comma in between: ").strip().split(','))

                for i in range(0,int(hospitalAmount)):
                    hospitals.append([hospitalCode[i], hospitalName[i]])
                
                writeToFile("hospitals.txt", sorted(hospitals))
                print("Initializing complete")
                break

            except IndexError:
                print("\nError in input, please try again.\n")

            except Exception as e:
                print(e)
    return

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
    flag = True
    while flag:
        print("\nWelcome to Admin panel")
        print("1. Add New User")
        print("2. Delete User")
        print("3. Search User")
        print("4. Modify User")
        print("5. List User")
        print("6. Quit")
        
        choice = input("Select one: ")
        match choice:
            case "1":
                addUser()
            case "2":
                delUser(loginInfo)
            case "3":
                searchUser()
            case "4":
                flag = modifyUser(loginInfo)
            case "5":
                listUsers()
            case "6":
                break
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
            case "2":
                userType = "Staff"
            case "3":
                break
            case _:
                print("Choice entered not valid, pls try again")
                continue
            
        while True:
            newUserID = input("Please enter your userID: ")
            newName = input("Please enter your name: ")
            newPwd = input("Please enter your password: ")
            
            if newUserID == "" or newName == "" or newPwd == "":
                print("Please fill in all the details.\n")
                continue

            users = [newUserID, newName, userType, newPwd]
            original = None
            duplicateUserDetected = False
            
            original = readFile("users.txt")

            for user in original:
                if user[0] == newUserID:
                    print("\nThis userID already exists.\n")
                    duplicateUserDetected = True

            if not duplicateUserDetected:
                original.append(users)
                writeToFile('users.txt',original)
                print("\nAdded New User")
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
                print("User doesn\'t exist")

            else:
                if users[int(delete)  - 1][0] == loginInfo[1]:
                    print("You cannot delete yourself.")
                    continue
                else:
                    users.pop(int(delete) - 1)

                writeToFile("users.txt",users)

                print("User deleted\n")
                break
    

def searchUser():
    while True:
        userFound = False
        searchTerm = input("\nSearch user by their userID(Type \"Quit\" to quit):")
        if searchTerm == "Quit":
            break
        
        users = readFile("users.txt")
        for user in users:
            if user[0] == searchTerm:
                print(f"Found user: {user[0]}\nName: {user[1]}\nType: {user[2]}")
                userFound = True

        if not userFound:
            print(f"User code {searchTerm} not found")

def modifyUser(loginInfo):
    flag = True
    while flag:
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
                print("User doesn't exist")

            else:
                while flag:
                    print("\nSelect the action to perform(Type \"Quit\" to quit):")
                    print("1. Change user type")
                    print("2. Change password")

                    choice = input()

                    try:
                        if choice == "Quit":
                            break
                        elif choice == "1":
                            while flag:
                                print("\nSelect one(Admin, Staff ; Type \"Quit\" to quit):")
                                changeType = input()
                                match changeType:
                                    case "Admin":
                                        users[mod - 1][2] = "Admin"
                                        writeToFile("users.txt",users)
                                        break
                                    case "Staff":
                                        print(users[mod - 1][0], loginInfo[1])
                                        if mod == 1:
                                            print("This account is the master account, you cannot change the type of it")
                                            continue

                                        elif users[mod - 1][0] == loginInfo[1] and users[mod - 1][2] == "Admin":
                                            specialChoice = input("If you change yourself to staff you will need to restart the program, proceed?(Yes/No): ")
                                            match specialChoice:
                                                case "Yes":
                                                    users[mod - 1][2] = "Staff"
                                                    writeToFile("users.txt",users)
                                                    flag = False
                                                    loginInfo[3] = 'Staff'
                                                    break
                                                
                                                case "No":
                                                    continue
                                                
                                                case _:
                                                    print("Choice not valid, please try again")
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
    return False
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
        print("3. List Hospitals")
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
                    supplier()
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
    print("Welcome to PPE Inventory Management System")
    print("Type \"quit\" to quit the program\n")  
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
            elif userID == "quit":
                quit()
        print("User doesn\'t exist, pls try again.\n")

def inventoryInit():
    supplierInitialize()
    hospitalInitialize()
    try:
        open("ppe.txt", "r")       
    except FileNotFoundError:
        while True:
            ppes = []
            
            try:
                print("\nPlease enter the details of 6 PPE Items.")
                print("Example: AA,BB,CC,DD,EE,FF\n")
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
        print("5. Search Transaction Detail of an Item")
        print("6. Quit")

        lessThan25()
        
        choice = input("\nSelect one: ")
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
                listStock()
                search()
            case "6":
                break
            case _:
                print("Choice entered not valid, pls try again")

def lessThan25():
    ppes = readFile("ppe.txt")
    itemLessThan25 = []
    print("Reminder: Items less than 25 boxes")

    for ppe in ppes:
        if int(ppe[3]) < 25:
            itemLessThan25.append(ppe[1])

    if itemLessThan25 == []:
        print(None)
    else:
        for i in itemLessThan25:
            print(i, end=' ')

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

def search():
    ppes = readFile("ppe.txt")
    
    while True:
        item = input("Please enter the item code(Type \"Quit\" to quit): ")

        if item == "Quit":
            break

        if not doesItemExists(item, ppes):
            print("Item doesn't exist, please try agian")
            continue
        
        transactions = readFile("transaction.txt")
        print(f"\n{'Transaction Time' : <30}{'Item Name' : ^20}{'Item Code' : ^20}{'Item Quantity' : ^15}{'Supplier or Hospital Code' : ^40}{'Status' : ^10}")

        for v in transactions:
            if item == v[2]:
                print(f"{v[0] : <30}{v[1] : ^20}{v[2] : ^20}{v[3] : ^15}{v[4] : ^40}{v[5] : ^10}")

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
                            continue
                            
                    transactionBetweenTimePeriod(sDateDT,eDateDT)
                    break
                
def transactionBetweenTimePeriod(startDate, endDate):
    transactions = readFile("transaction.txt")
    transactionDates = []

    for transaction in transactions:
        transactionDates.append(convStrToDT(transaction[0]))

    print(f"\n{'Transaction Date' : ^26}{'Item Name' : ^20}{'Item Code' : ^20}{'Quantity' : ^20}{'Supplier Or Hospital Code' : ^25}{'Status' : ^20}")
    for k, date in enumerate(transactionDates):
        if date >= startDate and date <= endDate:
            # filteredTransactions.append(k)
            print(f"{transactions[k][0] : <26}{transactions[k][1] : ^20}{transactions[k][2] : ^20}{transactions[k][3] : ^20}{transactions[k][4] : ^25}{transactions[k][5] : ^20}")

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
        
def supplier():
    supplierInitialize()
    while True:
        print("\nWelcome to supplier details")
        print("1. List Supplier Details")
        print("2. Change Supplier Name")
        print("3. Change Supplier Contact Number")
        print("4. Quit")

        choice = input("Select one: ")

        if choice == "4":
            break

        match choice:
            case "1":
                listSuppliers()
                continue
            case "2":
                suppliers = readFile("suppliers.txt")
                listSuppliers()

                while True:
                    print("Select the supplier you want to change(Supplier Code, Type \"Quit\" to quit):")
                    supToChange = input()

                    if supToChange == "Quit":
                        break

                    if not doesItemExists(supToChange, suppliers):
                        print("Supplier doesn't exist please try again")
                        continue

                    for k,v in enumerate(suppliers):
                        if v[0] == supToChange:
                            suppliers[k][1] = input("Enter the new name:")
                            writeToFile("suppliers.txt", suppliers)
                            print("New name changed")
                            break
            case "3":
                suppliers = readFile("suppliers.txt")
                listSuppliers()

                while True:
                    print("Select the supplier you want to change(Supplier Code, Type \"Quit\" to quit):")
                    supToChange = input()

                    if supToChange == "Quit":
                        break

                    if not doesItemExists(supToChange, suppliers):
                        print("Supplier doesn't exist please try again")
                        continue

                    for k,v in enumerate(suppliers):
                        if v[0] == supToChange:
                            suppliers[k][2] = input("Enter the new contact number:")
                            writeToFile("suppliers.txt", suppliers)
                            print("Contact number changed")
                            break

            case _:
                print("Choice entered is not valid, please try again")

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
    hospitalInitialize()
    hospitals = readFile("hospitals.txt")
    print(f"\n{'Hospital Code' : <15}{'Hospital Name' : ^40}")

    for v in hospitals:
        print(f"{v[0] : <15}{v[1] : ^40}")
        
def listSuppliers():
    suppliers = readFile("suppliers.txt")
    print(f"\n{'Supplier Code' : <15}{'Supplier Name' : ^25}{'Supplier Contact' : ^20}")

    for v in suppliers:
        print(f"{v[0] : <15}{v[1] : ^25}{v[2] : ^20}")

def main():
    initCheck()
    while True:
        # loginStatus, userID, userName, userType
        loginInfo = loginMenu()

        print(f"\nWelcome {loginInfo[2]}")

        mainMenu(loginInfo)

if __name__ == "__main__":
    main()
