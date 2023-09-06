# HO YAN XUN
# TP073669

# Check if the program is running the first time
# Checks by detecting the existence of ppe.txt and other files
def initCheck():
    try:
        with open('ppe.txt', "r") as file:
            print(file)
    except FileNotFoundError:
        print("File not found")
    
    isFirst = False

    if isFirst:
        initialization()

# Creates ppe.txt and propmts user to input the items
def initialization():
    pass

def loginMenu():
    pass

def mainMenu():
    pass

def main():
    initCheck()
    pass

if __name__ == "__main__":
    main()
