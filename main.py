# Jayden Yap p2112790 DSAA CA1
# Main program to run menu system
#import modules
from Stack import Stack #stack data structure

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

#function to print out current menu tree
def printTree():
    #print current menu tree
    treeString='\n*********************************************************\n* '
    n=54 #counter for number of spaces left in string (for formatting)
    x=0
    for i in menuTree.items:
        if(x>0): #if not first menu
            n-=3 #subtract spaces
            treeString+=' > '
        n-=len(f'{i}') #subtract length of string from number of spaces left 
        treeString+= f'{i.upper()}'
        x+=1
    for i in range(n):
        treeString+=' '
    treeString+='*'
    print(treeString)

#function to print out any menu based on dictionary (dict contains menu options)
def printMenu(menuDict):
    #printing the options
    for key in sorted(menuDict.keys()):
        for i in menuTree.items:
            print('\t',end=" ") #Indent depending on which level of menu we're at
        print(f'{key}: {menuDict[key][0]}')
    
    #get user input
    listOfOptions=[key for key in menuDict.keys()]
    optionsString=''
    i=0 #counter
    for x in listOfOptions:
        optionsString+=f'{x}'
        i+=1 #increment counter
        if i!=len(listOfOptions):
            optionsString+=','   
    userAnswer = int(input(f'Please select your choice: ({optionsString}) ').strip()) #strip to remove any whitespace
    nextMenu=menuDict.get(userAnswer)
    if nextMenu==None:
        print(f"\n\n{userAnswer} is a Invalid Answer!")
        input('Press enter to continue...\n\n')
        printMenu(menuDict) #recursion (restart menu)
    else:
        if len(nextMenu)>2: #list more than 2 means we are going back to another menu
            menuBack(nextMenu[2]) #set menu tree backwards
            nextMenu[1]() #then execute next menu function
        else:
            nextMenu[1]() #execute given function



#functions to init menu dictionaries and then print them
def mainMenu():
    menuTree.push('MAIN')
    mainMenuDict =  {
    1: ["New", newThesaurus],
    2: ["Open", openThesaurus],
    3: ["Sort", sortMenu],
    4: ["Process Text",processText],
    # 5: ["Extra Option One",None], #to be added (find keyword corresponding to given synonym?)
    # 6: ["Extra Option Two",None], #to be added (change keyword/synonyms?)
    7: ["Print",printThesaurus],
    8: ["Save",saveThesaurus],
    9: ["Save As",saveAsThesaurus],
    10: ["Exit", exitSystem]
    }
    printTree()
    printMenu(mainMenuDict)

def newThesaurus():
    print('hello')

def openThesaurus():
    print('hi again')

def sortMenu():
    menuTree.push('SORT')
    sortMenuDict = {
        1: ['Alphabetically (Default)',None],
        2: ['Length/Alphabetically',None],
        3: ['Length/Random Alphabetically',None],
        4: ['Randomly',None],
        5: ['Back to Main Menu', mainMenu,2], #2 indicate we are going back by 1 menu (pop from stack twice)
        10: ["Exit", exitSystem]
    }
    printTree()
    printMenu(sortMenuDict)

def processText():
    print('hi again again')

def printThesaurus():
    print('printing thesaurus')

def saveThesaurus():
    print('saving thesaurus')

def saveAsThesaurus():
    print('saving thesaurus as something')


#menuTree is a system to keep track of which menu you're in (example Main>Sort>Alphabetical etc)
def menuBack(times):
    for i in range(times):
        menuTree.pop()

menuTree=Stack()
mainMenu()
# welcomeMenu()

