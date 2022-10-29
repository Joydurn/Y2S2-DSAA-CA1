# Jayden Yap p2112790 DSAA CA1
# Main program to run menu system

# #Welcome message
# def welcomeMenu():
#     print('''
# *********************************************************
# * ST1507 DSAA: Welcome to:                              *
# *                                                       *
# * ~ Thesaurus Based Text Processing Application ~       *
# *_______________________________________________________*
# *                                                       *
# * ~ Done by: Jayden Yap (2112790)                       *
# * ~ Class DAAA/2B/04                                    *
# *********************************************************
# ''')
#     input('Press enter to continue...\n\n')
#     mainMenu() #proceed to main menu

#function called when quit system is called 
def exitSystem():
    print('\nProgram closing... Goodbye!\n')
    raise SystemExit

#function to print out any menu based on dictionary (dict contains menu options)
def printMenu(menuDict):
    listOfOptions=[key for key in menuDict.keys()]
    optionsString=''
    i=0 #counter
    for x in listOfOptions:
        optionsString+=f'{x}'
        i+=1 #increment counter
        if i!=len(listOfOptions):
            optionsString+=','
    print(f'\nPlease select your choice: ({optionsString})')
    for key in sorted(menuDict.keys()):
        print(f'\t\t{key}: {menuDict[key][0]}')
    userAnswer = int(input("Enter choice: ").strip()) #strip to remove any whitespace
    nextMenu=menuDict.get(userAnswer)
    if nextMenu==None:
        print(f"\n\n{userAnswer} is a Invalid Answer!")
        input('Press enter to continue...\n\n')
        printMenu(menuDict) #recursion (restart menu)
    else:
        if len(nextMenu)>2: #list more than 2 means we're going into another submenu
            nextMenu[1](nextMenu[2]) #execute printmenu function with another menu 'dictionary' 
        else:
            nextMenu[1]() #execute given function

#functions to init menu dictionaries and then print them
def mainMenu():
    mainMenuDict =  {
    1: ["New", newThesaurus],
    2: ["Open", openThesaurus],
    3: ["Sort", sortMenu],
    # "4": ["Process Text",processText],
    # "5": ["Extra Option One",None], #to be added (find keyword corresponding to given synonym?)
    # "6": ["Extra Option Two",None], #to be added (change keyword/synonyms?)
    # "7": ["Print",printThesaurus],
    # "8": ["Save",saveThesaurus],
    # "9": ["Save As",saveAsThesaurus],
    10: ["Exit", exitSystem]
    }
    printMenu(mainMenuDict)

def sortMenu():
    sortMenuDict = {
        1: ['Alphabetically (Default)',None],
        2: ['Length/Alphabetically',None],
        3: ['Length/Random Alphabetically',None],
        4: ['Randomly',None],
        5: ['Back to Main Menu', mainMenu],
        10: ["Exit", exitSystem]
    }
    printMenu(sortMenuDict)

def newThesaurus():
    print('hello')

def openThesaurus():
    print('hi again')

mainMenu()
# welcomeMenu()

