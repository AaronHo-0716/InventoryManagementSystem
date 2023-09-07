# HO YAN XUN
# TP073669

# Check if the program is running the first time
# Checks by detecting the existence of ppe.txt and other files
def initCheck():
    isFirst = False
    try:
        with open('ppe.txt', "r") as file:
            print(file)
    except FileNotFoundError:
        print("Initializing system...")
        isFirst = True

    if isFirst:
        initialization()

# Creates ppe.txt and propmts user to input the items
def initialization():
    print("initialization complete.")

def loginMenu():
    pass

def mainMenu():
    choice = input()
    try:
        int(choice)
    except:
        print("Error, pls try again")
    else:
        match int(choice):
            case 5:
                quit()

def main():
    initCheck()
    while True:
        mainMenu()

if __name__ == "__main__":
    main()
