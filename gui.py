# Jayden Yap p2112790 DSAA CA1
# Main program to run menu system
#import modules
from os import listdir
from stack import Stack
from thesaurus import Thesaurus
thesaurus=Thesaurus()
menuTree=Stack()
class GUI:
    def __init__(self):
        self.__name='Jayden Yap'
        self.__studentID='2112790'
        self.__courseClass='DAAA/2B/04'
        self.__fileName=None

    def welcomeMenu(self):
        print(f'''
    *********************************************************
    * ST1507 DSAA: Welcome to:                              *
    *                                                       *
    * ~ Thesaurus Based Text Processing Application ~       *
    *_______________________________________________________*
    *                                                       *
    * ~ Done by: {self.__name} ({self.__studentID})                       *
    * ~ Class {self.__courseClass}                                *
    *********************************************************
    ''')
        input('Press enter to continue...\n\n')
        self.mainMenu() #proceed to main menu
        #function called when quit system is called 

    def __exitSystem(self):
        if thesaurus.size()!=0:
            print('WARNING: A thesaurus is already loaded, proceeding will delete the previous thesaurus (unless it was already saved)')
            while True:
                answer=input('Proceed? (y/n): ')
                if answer=='y':
                    break #proceed to create
                elif answer=='n':
                    print('Going back to main menu...')
                    self.mainMenu()
                else:
                    print('Invalid answer, try again... \n')
        print('\nProgram closing... Goodbye!\n')
        raise SystemExit

    #function to print out current menu tree
    def __printTree(self):
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
        treeString+='*\n'
        print(treeString)

    #function to print out any menu based on dictionary (dict contains menu options)
    def __printMenu(self,menuList):
        #printing the options
        for index,list in enumerate(menuList):
            for i in range(len(menuTree.items)-1): #only indent if on 2nd level menu
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
        #first check if integer and not out of range
        if userAnswer.isnumeric() and int(userAnswer)<=len(menuList) and int(userAnswer)>0:
            userAnswer=int(userAnswer)
            nextFunctionList=menuList[(userAnswer-1)]
            #then go to next menu/function
            nextFunctionList[1]() #execute given function
            #if function returns here then redirect to main menu again
            self.__printTree()
            self.__printMenu(menuList)
        else:
            print(f"\n\n{userAnswer} is a Invalid Answer!")
            input('Press enter to continue...\n\n')
            self.__printTree()
            self.__printMenu(menuList) #recursion (restart menu)
    
    
    #function when printing thesaurus (option 7)
    def __printThesaurus(self):
        if thesaurus.size()==0: #if no thesaurus
            print('ERROR: No thesaurus found, try creating or opening one first, Returning to main menu')
            input('Press enter to continue...\n\n')
            self.mainMenu()
        menuTree.push('Print')
        self.__printTree()
        fullList=thesaurus.getFullThesaurus()
        print('Printing Thesaurus now:\n')
        print(thesaurus.getStringFormat())
        input('Press enter to continue...\n')
        self.mainMenu()
        




    #functions to init menu dictionaries and then print them'
    #REMEMBER TO PRIVATE THIS FUNCTION LATER
    def mainMenu(self):
        menuTree.items=['MAIN']
        mainMenuList =  [
        ["New", self.__createNew],
        ["Open", self.__openThesaurus],
        ["Sort", self.__sortMenu],
        ["Process Text",self.processText],
        ["Extra Option One",None], #to be added (find keyword corresponding to given synonym?)
        ["Extra Option Two",None], #to be added (change keyword/synonyms?)
        ["Print",self.__printThesaurus],
        ["Save",self.__saveThesaurus],
        ["Save As",self.__saveAsThesaurus],
        ["Exit", self.__exitSystem]
        ]
        self.__printTree()
        self.__printMenu(mainMenuList)

    def __sortMenu(self):
        def sortAlpha():
            print('Sorting synonyms Alphabetically...')
            thesaurus.sortAlphabetically()
            self.__printThesaurus()

        def sortLenAlpha():
            print('Sorting synonyms first by Length, then Alphabetically...')
            thesaurus.sortLengthAlphabetically()
            self.__printThesaurus()

        def sortLenRand():
            print('Sorting synonyms first by Length, then randomly...')
            thesaurus.sortLengthAlphabetically()
            self.__printThesaurus()

        def sortRand():
            print('Sorting synonyms randomly...')
            thesaurus.sortRandomly()
            self.__printThesaurus()

        menuTree.push('SORT')
        sortMenuList = [
            ['Alphabetically (Default)',sortAlpha],
            ['Length/Alphabetically',sortLenAlpha],
            ['Length/Random Alphabetically',sortLenRand],
            ['Randomly',sortRand],
            ['Back to Main Menu', self.mainMenu], #2 indicate we are going back by 1 menu (pop from stack twice)
            ["Exit", self.__exitSystem]
        ]
        self.__printTree()
        self.__printMenu(sortMenuList)

    def processText(self):
        menuTree.push('Process Text')
        self.__printTree()
        print('hi again again')

    def __openThesaurus(self):
        menuTree.push('Open')
        self.__printTree()
        print('\tAvailable files:')
        print('\t'+', '.join(listdir('thesaurus'))) #tab followed by all filenames seperated by ', '
        print('\t(Type 1 to quit)')
        fileName=input('\tPlease enter full file name you want to open: (with .txt): ')
        if fileName=='1':
            self.mainMenu()
        else:
            try:
                with open(f"thesaurus/{fileName}","r") as f:
                    string=f.read() #read from file
                thesaurus.createFromString(string)
                print(f'Successfully read Thesaurus from file "{fileName}"')
                self.__printThesaurus()
                self.__fileName=fileName
            except Exception as e:
                print(e)
                print('Please try again...')
                input('Press enter to continue...')
                menuTree.pop()
                self.__openThesaurus()
            
    def __saveThesaurus(self):
        if thesaurus.size()==0: #if no thesaurus
            print('ERROR: No thesaurus found, try creating or opening one first, Returning to main menu')
            input('Press enter to continue...\n\n')
            self.mainMenu()
        menuTree.push('Save Thesaurus')
        self.__printTree()
        print('saving thesaurus')

    def __saveAsThesaurus(self):
        if thesaurus.size()==0: #if no thesaurus
            print('ERROR: No thesaurus found, try creating or opening one first, Returning to main menu')
            input('Press enter to continue...\n\n')
            self.mainMenu()
        menuTree.push('Save As')
        self.__printTree()
        print('(Type 1 to quit)')
        newFileName=input(f'Please enter filename: ').strip()
        if newFileName=='1': 
            self.mainMenu()
        else:
            while True: 
                confirm=input(f'Are you sure you want to save to /thesaurus/{newFileName}.txt? (y/n): ').strip().lower()
                if confirm=='n':
                    print('Going back to main menu!')  #go back to start 
                    input('Press enter to continue...')
                    self.mainMenu()
                elif confirm=='y':
                    thesaurusString=thesaurus.getStringFormat()
                    try:
                        with open(f"thesaurus/{newFileName}.txt","x") as f:
                            f.write(thesaurusString) #write to file
                        print('Save Complete! Going back to main menu...')
                        input('Press enter to continue...')
                        self.mainMenu()
                    except Exception as e:
                        error=e.args[0] #get error code
                        if error==22:
                            print(f'Invalid Filename! "{newFileName}.txt"')
                        elif error==17:
                            print(f'File already exists!')
                        else:
                            print(e)
                        input('Press enter to continue...')
                        menuTree.pop() 
                        self.__saveAsThesaurus()
                else:
                    print('Invalid answer! Please try again...')
                    print('Press enter to continue')
                
    def __createNew(self):
        #nested functions used later
        def __getKeySynPair(keywordCount):
            #get keyword
            keyInvalid=True 
            while keyInvalid:
                print('\t(Type 1 if done with this Thesaurus, type 2 to quit)')
                keyword=input(f'\tEnter {self.__makeOrdinal(keywordCount)} keyword: ').strip().lower() 
                if keyword=='1':
                    __finishThesaurus()
                elif keyword=='2':
                    self.mainMenu()
                else:
                    keyInvalid=__keyIsInvalid(keyword)
            #now get synonyms
            synList=[]
            synCount=1 #counter
            while True: #while not done entering synonyms: 
                #check if valid 
                synInvalid=True
                while synInvalid:
                    print('\t\t(Type 1 if done with this keyword, type 2 to quit)')
                    synonym=input(f'\t\tEnter {self.__makeOrdinal(synCount)} synonym for {keyword}: ').strip().lower() 
                    if synonym in ['1','2']:
                        break
                    synInvalid=__synIsInvalid(keyword,synonym,synList)
                if synonym=='1':
                    break 
                elif synonym=='2':
                    self.mainMenu()
                #add synonym 
                synList.append(synonym)
                synCount+=1
            return (keyword,synList) #return keyword and synonym list pair as tuple
        #function to check if keys are valid
        def __keyIsInvalid(keyword):
            if keyword in thesaurus.getKeywords():
                print('\tKeyword already exists, please try again...')
                return True
            elif any(keyword in sublist for sublist in thesaurus.getAllSynonyms()): 
                print('\tKeyword already exists as a synonym, please try again...')
                return True
            elif not keyword.isalpha(): #check if has numbers/symbols
                print('\tOnly letters allowed, no numbers,symbols or spaces, try again')
                return True
            else:
                return False
        #function to check if synonym is valid, more lenient than for keyword
        def __synIsInvalid(keyword,synonym,synList):
            if synonym in thesaurus.getKeywords() or synonym==keyword:
                print('\t\tSynonym is already a keyword! Please try again...')
                return True
            elif synonym in synList: #if was already entered
                print('\t\tSynonym already entered, please try again...')
                return True
            elif any(synonym in sublist for sublist in thesaurus.getAllSynonyms()): 
                print('\t\tSynonym already exists for another keyword, please try again...')
                return True
            elif not synonym.isalpha(): #check if has numbers/symbols
                print('\t\tOnly letters allowed, no numbers or symbols, try again')
                return True
            else:
                return False
        def __finishThesaurus():
            #check if there are keywords
            if thesaurus.size()==0:
                input('No keywords entered! Press enter to continue...')
                return 
            else:
                print('Your new Thesaurus is ready! Here it is...')
                #sort alphabetically by default
                thesaurus.sortAlphabetically()
                thesaurus.sortKeywords()
                self.__printThesaurus()
                self.mainMenu()

        menuTree.push('New Thesaurus')
        self.__printTree()
        #check if thesaurus exists already
        if thesaurus.size()!=0:
            print('\tWARNING: A thesaurus is already loaded, proceeding will delete the previous thesaurus (unless it was already saved)')
            while True:
                answer=input('\tProceed? (y/n): ')
                if answer=='y':
                    break #proceed to create
                elif answer=='n':
                    print('\tGoing back to main menu...')
                    self.mainMenu()
                else:
                    print('\tInvalid answer, try again... \n')
        #refresh thesaurus to empty
        thesaurus.refresh()
        keywordCount=0
        while True:
            keywordCount+=1
            keyword,synList = __getKeySynPair(keywordCount) #pass keyword count into function
            thesaurus.addKeySynPair(keyword, synList)
            print(f'\tAdded keyword "{keyword}" with the following synonyms: {synList}\n')
    
    def __makeOrdinal(self,n):
        '''
        Convert an integer into its ordinal version:
            __makeOrdinal(1)   -> '1st'
            __makeOrdinal(3)   -> '3rd'
            __makeOrdinal(122) -> '122nd'
        '''
        n = int(n)
        if 11 <= (n % 100) <= 13:
            suffix = 'th'
        else:
            suffix = ['th', 'st', 'nd', 'rd', 'th'][min(n % 10, 4)]
        return str(n) + suffix