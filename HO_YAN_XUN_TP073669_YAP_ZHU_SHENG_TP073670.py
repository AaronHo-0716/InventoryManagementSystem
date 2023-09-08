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


def mainMenu():
    choice = input()
    try:
        int(choice)
    except:
        print("Value entered not a valid integer, pls try again")
    else:
        match int(choice):
            case 5:
                quit()

def loginMenu():
    userID = input("Please enter your userID: ")
    password = input("Please enter your password: ")
        
    try:
        with open('users.txt', 'r') as f:
            users = eval(f.read())

            for user in users:
                if userID == user["userID"] and password == user["password"]:
                    return {"loginStatus": True, "userID": userID, "userType": user["userType"]} 
                
    except:
        print("Login error, pls try again")
        return {"loginStatus": False, "userID": None, "userType": None} 
    else:
        print("Wrong userID or password, pls try again")
        return {"loginStatus": False, "userID": None, "userType": None} 

def main():
    loginInfo = {"loginStatus": False, "userID": None, "userType": None}
    
    initCheck()
    while not loginInfo["loginStatus"]:
        loginInfo = loginMenu()

    print(f"You are logined as {loginInfo['userType']}, your ID is {loginInfo['userID']}")
    
    while True:
        mainMenu()

if __name__ == "__main__":
    main()
