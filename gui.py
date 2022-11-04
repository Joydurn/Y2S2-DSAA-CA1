# Jayden Yap p2112790 DSAA CA1
# Main program to run menu system
#import modules
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
class GUI:
    def __init__(self) -> None: pass

    #function called when quit system is called 
    def exitSystem(self):
        print('\nProgram closing... Goodbye!\n')
        raise SystemExit

    #function to print out current menu tree
    def printTree(self):
        #print current menu tree
        treeString='\n*********************************************************\n* '
        n=54 #counter for number of spaces left in string (for formatting)
        x=0
        for i in self.menuTree.items:
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
    def printMenu(self,menuList):
        #printing the options
        for index,list in enumerate(menuList):
            for i in self.menuTree.items:
                print('\t',end=" ") #Indent depending on which level of menu we're at
            print(f'{index+1}: {list[0]}')
        
        listOfOptions = range(1,len(menuList)+1)
        optionsString=''
        i=0 #counter
        for x in listOfOptions:
            optionsString+=f'{x}'
            i+=1 #increment counter
            if i!=len(listOfOptions):
                optionsString+=','   
        userAnswer = input(f'\nPlease select your choice ({optionsString}): ').strip() #strip to remove any whitespace
        #first check if integer
        if userAnswer.isnumeric() and int(userAnswer)<=len(menuList):
            userAnswer=int(userAnswer)
            nextFunctionList=menuList[(userAnswer-1)]
            #then go to next menu/function
            if len(nextFunctionList)>2: #list more than 2 means we are going back to another menu
                self.menuBack(nextFunctionList[2]) #set menu tree backwards
                nextFunctionList[1]() #then execute next menu function
                
            else:
                nextFunctionList[1]() #execute given function
                #if function returns here then redirect to main menu again
                self.printTree()
                self.printMenu(menuList)
        else:
            print(f"\n\n{userAnswer} is a Invalid Answer!")
            input('Press enter to continue...\n\n')
            self.printTree()
            self.printMenu(menuList) #recursion (restart menu)
        

    #functions to init menu dictionaries and then print them
    def mainMenu(self):
        self.menuTree.push('MAIN')
        mainMenuList =  [
        ["New", Thesaurus.createNew],
        ["Open", self.openThesaurus],
        ["Sort", self.sortMenu],
        ["Process Text",self.processText],
        ["Extra Option One",None], #to be added (find keyword corresponding to given synonym?)
        ["Extra Option Two",None], #to be added (change keyword/synonyms?)
        ["Print",Thesaurus.printThesaurus],
        ["Save",Thesaurus.saveThesaurus],
        ["Save As",Thesaurus.saveAsThesaurus],
        ["Exit", self.exitSystem]
        ]
        self.printTree()
        self.printMenu(mainMenuList)

    def newThesaurus(self):
        self.menuTree.push('New')
        self.printTree()
        print('hello')

    def openThesaurus(self):
        self.menuTree.push('Open')
        self.printTree()
        print('hi again')

    def sortMenu(self):
        self.menuTree.push('SORT')
        sortMenuList = [
            ['Alphabetically (Default)',None],
            ['Length/Alphabetically',None],
            ['Length/Random Alphabetically',None],
            ['Randomly',None],
            ['Back to Main Menu', self.mainMenu,2], #2 indicate we are going back by 1 menu (pop from stack twice)
            ["Exit", self.exitSystem]
        ]
        self.printTree()
        self.printMenu(sortMenuList)

    def processText(self):
        self.menuTree.push('Process Text')
        self.printTree()
        print('hi again again')

    def saveThesaurus(self):
        self.menuTree.push('Save')
        self.printTree()
        print('saving thesaurus')

    def saveAsThesaurus(self):
        self.menuTree.push('Save As')
        self.printTree()
        print('saving thesaurus as something')

    #menuTree is a system to keep track of which menu you're in (example Main>Sort>Alphabetical etc)
    def menuBack(self,times):
        for i in range(times):
            self.menuTree.pop()
    
    # welcomeMenu()

