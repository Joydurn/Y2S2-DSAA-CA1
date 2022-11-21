# Jayden Yap p2112790 DAAA/2B/04 DSAA CA1 gui.py
# Main program to run menu system
#import modules
from os import listdir
from stack import menuStackLL
from thesaurus import Thesaurus
thesaurus=Thesaurus()
menuStack=menuStackLL()
class GUI:
    def __init__(self):
        self.__name='Jayden Yap'
        self.__studentID='2112790'
        self.__courseClass='DAAA/2B/04'
        self.__fileName=None #file name to be loaded if a file is opened

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
        self.__mainMenu() #proceed to main menu
        #function called when quit system is called 

    def __exitSystem(self):
        if not thesaurus.isEmpty():
            print('WARNING: A thesaurus is already loaded, proceeding will delete the previous thesaurus (unless it was already saved)')
            while True:
                answer=input('Proceed? (y/n): ')
                if answer=='y':
                    break #proceed to create
                elif answer=='n':
                    print('Going back to main menu...')
                    self.__mainMenu()
                else:
                    print('Invalid answer, try again... \n')
        print('\nBye, thanks for using ST1507 DSAA: Thesaurus Based Text Processor\n')
        raise SystemExit

    #function to print out current menu stack
    def __printStack(self):
        #print current menu stack
        stackString='*'*54+'\n* ' 
        menusString=''
        for index,node in enumerate(menuStack): 
            item=node.element
            if index>0:
                menusString+=' < ' #add connector if not first menu
            menusString+=f'{item.upper()}'
        stackString+=menusString.ljust(51) #add padding for formatting
        stackString+='*\n'
        #print file name of thesaurus (if present)
        if self.__fileName is not None: 
            loadedString=f'* LOADED: {self.__fileName}'
            stackString+=loadedString.ljust(53)+'*\n'
        elif not thesaurus.isEmpty(): #if thesaurus was created
            stackString+='* THESAURUS LOADED'.ljust(53)+'*\n'
        print(stackString)

    #function to print out any menu based on dictionary (dict contains menu options)
    def __printMenu(self,menuList):
        #printing the options
        for index,subList in enumerate(menuList):
            if menuStack.size>1: #if we on at least 2nd level of menu
                print('\t',end=" ") #Indent text
            print(f'{index+1}: {subList[0]}')
        
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
            self.__printStack()
            self.__printMenu(menuList)
        else:
            print(f"\n\n{userAnswer} is a Invalid Answer!")
            input('Press enter to continue...\n\n')
            self.__printStack()
            self.__printMenu(menuList) #recursion (restart menu)
    
    
    #function when printing thesaurus (option 7)
    def __printThesaurus(self):
        menuStack.push('Print')
        self.__printStack()
        fullList=thesaurus.getFullThesaurus()
        print('Printing Thesaurus now:\n')
        print(thesaurus.getStringFormat())
        input('Press enter to continue...\n')
        self.__mainMenu()


    #functions to init menu dictionaries and then print them'
    #REMEMBER TO PRIVATE THIS FUNCTION LATER
    def __mainMenu(self):
       
        menuStack.resetToMain()
        mainMenuList =  [
        ["New", self.__createNew],
        ["Open", self.__openThesaurus],
        ["Exit", self.__exitSystem]
        ]
        #we will append options to the list depending on some conditions
        if not thesaurus.isEmpty(): #if thesaurus is loaded
            mainMenuList.insert(2,["Sort", self.__sortMenu])
            mainMenuList.insert(3,["Process Text",self.__inputTextMenu])
            mainMenuList.insert(4,["Find Synonym",self.__getSynonymFromWord])
            mainMenuList.insert(5,["Edit Thesaurus",self.__editThesaurusMenu])
            mainMenuList.insert(6,["Print",self.__printThesaurus])
            if self.__fileName is not None: #if thesaurus was loaded from a file, Save option should be visible
                mainMenuList.insert(7,["Save",self.__save])
                mainMenuList.insert(8,["Save As",self.__saveAs])
            else:
                mainMenuList.insert(7,["Save As",self.__saveAs])
            
        self.__printStack()
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

        sortMenuList = [
            ['Alphabetically (Default)',sortAlpha],
            ['Length/Alphabetically',sortLenAlpha],
            ['Length/Random Alphabetically',sortLenRand],
            ['Randomly',sortRand],
            ['Back to Main Menu', self.__mainMenu],
        ]
        menuStack.push('SORT')
        self.__printStack()
        self.__printMenu(sortMenuList)

    def __inputTextMenu(self):
        def inputText():
            menuStack.push('Input')
            self.__printStack()
            print('\t(Type 1 to quit)')
            inputText=input('\tPlease input the text you want to process:\n\t')
            if inputText=='1':
                self.__mainMenu()
            else:
                self.__processTextMenu(inputText)

        def __openText():
            menuStack.push('Open')
            self.__printStack()
            print('\tAvailable files:')
            print('\t'+', '.join(listdir('text'))) #tab followed by all filenames seperated by ', '
            print('\t(Type 1 to quit)')
            fileName=input('\tPlease enter full file name you want to open: (with .txt):\n\t')
            if fileName=='1':
                self.__mainMenu()
            else:
                try:
                    with open(f"text/{fileName}","r") as f:
                        string=f.read() #read from file
                    print(f'Successfully read text from file "{fileName}"')
                    print('Previewing now...')
                    print(string)
                    input('Press enter to continue...')
                    self.__processTextMenu(string)
                except Exception as e:
                    print(e)
                    print('Please try again...')
                    input('Press enter to continue...')
                    menuStack.pop()
                    __openText()

        menuStack.push('Processing')
        processTextMenuList=[
        ["Input your own Text",inputText],
        ["Open a text file",__openText],
        ["Back to Main Menu",self.__mainMenu]
        ]
        self.__printStack()
        self.__printMenu(processTextMenuList)

    def __processTextMenu(self,text):
        def __simpWriting():
            try:
                processed=thesaurus.simplifyString(text)
            except Exception as e: 
                print(e)
                print('Please try again...')
                input('Press enter to continue...')
                menuStack.pop()
                self.processTextMenu(text)
            print('\tConverted Text:')
            print(f'\t{processed}')
            __saveFile(processed)
            
            
        def __elegWriting():
            try:
                processed=thesaurus.elegantString(text)
            except Exception as e: 
                print(e)
                print('Please try again...')
                input('Press enter to continue...')
                menuStack.pop()
                self.processTextMenu(text)
            print('\tConverted Text:')
            print(f'\t{processed}')
            __saveFile(processed)

        def __saveFile(processed):
            userInput=input('\tDo you want to save text to a file? y/n: ')
            if userInput=='n':
                print('Going back to main menu...')
                self.mainMenu()
            elif userInput=='y':
                while True:
                    fileName=input('Enter a file name (excluding .txt): ')
                    try:
                        with open(f"text/{fileName}.txt","x") as f:
                            f.write(processed) #write to file
                        print('Save Complete! Going back to main menu...')
                        input('Press enter to continue...')
                        self.__mainMenu()
                    except Exception as e:
                        error=e.args[0] #get error code
                        if error==22:
                            print(f'Invalid Filename! "{fileName}.txt"')
                        elif error==17:
                            print(f'File already exists!')
                        else:
                            print(e)
                        input('Press enter to continue...')
                        menuStack.pop() 
                        __saveFile(processed)
            else:
                print("Invalid input, please try again...")
                input('Press enter to continue...')
                __saveFile(processed)

        menuStack.push('Process Text')
        processTextMenuList=[
        ["Simplified Writing",__simpWriting],
        ["Elegant Writing",__elegWriting],
        ["Back to Main Menu",self.__mainMenu]
        ]
        self.__printStack()
        self.__printMenu(processTextMenuList)


    def __openThesaurus(self):
        menuStack.push('Open')
        self.__printStack()
        print('\tAvailable files:')
        print('\t'+', '.join(listdir('thesaurus'))) #tab followed by all filenames seperated by ', '
        print('\t(Type 1 to quit)')
        fileName=input('\tPlease enter full file name you want to open: (with .txt):\n\t')
        if fileName=='1':
            self.__mainMenu()
        else:
            try:
                with open(f"thesaurus/{fileName}","r") as f:
                    string=f.read() #read from file
                thesaurus.createFromString(string)
                print(f'Successfully read Thesaurus from file "{fileName}"')
                self.__fileName=fileName
                thesaurus.sortKeywords() #sort the keywords alphabetically
                self.__printThesaurus()
            except Exception as e:
                print(e)
                print('Please try again...')
                input('Press enter to continue...')
                menuStack.pop()
                self.__openThesaurus()
            
    def __save(self):
        if thesaurus.isEmpty(): #if no thesaurus
            print('ERROR: No thesaurus found, try creating or opening one first, Returning to main menu')
            input('Press enter to continue...\n\n')
            self.__mainMenu()
        elif self.__fileName==None:
            print('No file loaded, redirecting to Save As function...')
            self.__saveAs()
        menuStack.push('Save Thesaurus')
        self.__printStack()
        answer=input(f'Are you sure you want to save/overwrite {self.__fileName}? y/n: ')
        if answer=='y':
            thesaurusString=thesaurus.getStringFormat()
            try:
                # with open(f"thesaurus/{self.__fileName}.txt", 'r') as file :
                #     filedata = file.read()
                # filedata=filedata.
                with open(f"thesaurus/{self.__fileName}","w") as f:
                    f.write(thesaurusString) #write to file
                print('\tSave Complete! Going back to main menu...')
                input('\tPress enter to continue...')
                self.__mainMenu()
            except Exception as e:
                error=e.args[0] #get error code
                if error==22:
                    print(f'\tInvalid Filename! "{self.__fileName}"')
                else:
                    print(e)
                input('\tPress enter to continue...')
                menuStack.pop() 
                self.__save()
        elif answer=='n':
            self.__mainMenu()
        else:
            print('Invalid answer, please try again!')
            input('Press enter to continue...')
            menuStack.pop()
            self.__save()

    def __saveAs(self):
        if thesaurus.size()==0: #if no thesaurus
            print('ERROR: No thesaurus found, try creating or opening one first, Returning to main menu')
            input('Press enter to continue...\n\n')
            self.__mainMenu()
        
        menuStack.push('Save As')
        self.__printStack()
        print('\tExisting files:')
        directory=listdir('thesaurus')
        print('\t'+', '.join(directory)) #tab followed by all filenames seperated by ', '
        print('\t(Type 1 to quit)')
        newFileName=input(f'\tPlease enter new filename (without .txt): ').strip()
        if newFileName=='1': 
            self.__mainMenu()
        else:
            while True: 
                if f'{newFileName}.txt' in directory: #if existing file name
                    print(f'\tWARNING: A file with name {newFileName}.txt already exists!')
                confirm=input(f'\tAre you sure you want to save to /thesaurus/{newFileName}.txt? (y/n): ').strip().lower()
                if confirm=='n':
                    menuStack.pop()
                    self.__saveAs()
                elif confirm=='y':
                    thesaurusString=thesaurus.getStringFormat()
                    try:
                        with open(f"thesaurus/{newFileName}.txt","w") as f:
                            f.write(thesaurusString) #write to file
                        print('\tSave Complete! Going back to main menu...')
                        self.__fileName=f'{newFileName}.txt'
                        input('\tPress enter to continue...')
                        self.__mainMenu()
                    except Exception as e:
                        error=e.args[0] #get error code
                        if error==22:
                            print(f'\tInvalid Filename! "{newFileName}.txt"')
                        else:
                            print(e)
                        input('\tPress enter to continue...')
                        menuStack.pop() 
                        self.__saveAs()
                else:
                    print('\tInvalid answer! Please try again...')
                    print('\tPress enter to continue')

    #function to check if keys are valid
    def __keyIsInvalid(self,keyword):
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
    def __synIsInvalid(self,keyword,synonym,synList):
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
                    self.__mainMenu()
                else:
                    keyInvalid=self.__keyIsInvalid(keyword)
            #now get synonyms
            synList=[]
            synCount=1 #counter
            while True: #while not done entering synonyms: 
                #check if valid 
                synInvalid=True
                while synInvalid:
                    if synCount>1: #if not first 1st synonym, allow to finish keyword
                        print('\t\t(Type 1 if done with this keyword, type 2 to quit)')
                    else: 
                        print('\t\t(Type 2 to quit)')
                    synonym=input(f'\t\tEnter {self.__makeOrdinal(synCount)} synonym for {keyword}: ').strip().lower() 
                    if synonym=='2' or (synCount>1 and synonym=='1'):
                        break
                    synInvalid=self.__synIsInvalid(keyword,synonym,synList)
                if synonym=='1':
                    break 
                elif synonym=='2':
                    self.__mainMenu()
                #add synonym 
                synList.append(synonym)
                synCount+=1
            return (keyword,synList) #return keyword and synonym list pair as tuple
            

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
                self.__mainMenu()

        menuStack.push('New Thesaurus')
        self.__printStack()
        #check if thesaurus exists already
        if thesaurus.size()!=0:
            print('\tWARNING: A thesaurus is already loaded, proceeding will delete the previous thesaurus (unless it was already saved)')
            while True:
                answer=input('\tProceed? (y/n): ')
                if answer=='y':
                    self.__fileName=None 
                    break #proceed to create
                elif answer=='n':
                    print('\tGoing back to main menu...')
                    self.__mainMenu()
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
    
    #EXTRA OPTION 1: Get synonym for any word
    def __getSynonymFromWord(self):
        menuStack.push('Get Synonym')
        self.__printStack()
        print('\t(Type 1 to quit)')
        word=input('\tPlease enter your input word: ')
        if word=='1':
            self.__mainMenu()
        else:
            synList=thesaurus.findSynonymFromWord(word)
            if synList is None:
                print('\tNo synonym found... please try again')
                input('\tPress enter to continue...')
                menuStack.pop()
                self.__getSynonymFromWord()
            else:
                print(f"\tHere are synonyms for '{word}':")
                for syn in synList:
                    print(f'\t{syn.title()}')
                input('\tPress enter to continue...')
                menuStack.pop()
                self.__getSynonymFromWord()

    #EXTRA OPTION 2: Edit thesaurus: [Add synonym to keyword or add keyword+synonyms]
    def __editThesaurusMenu(self):
        def addKeyword():
            menuStack.push('Add Keyword')
            self.__printStack()
            keyInvalid=True 
            while keyInvalid:
                print('\t(Type 1 to quit)')
                keyword=input('\tEnter a keyword to add: ').lower()
                if keyword=='1':
                    #pop twice
                    menuStack.pop()
                    menuStack.pop()
                    self.__editThesaurusMenu()
                else:
                    keyInvalid=self.__keyIsInvalid(keyword)
            
            #now we get synonyms
            synList=[]
            synCount=1 
            while True: 
                synInvalid=True 
                while synInvalid:
                    if synCount>1: #if not 1st synonym, then allow to finish keyword
                        print('\t\t(Type 1 if done with keyword, type 2 to quit)')
                    else:
                        print('\t\t(Type 2 to quit)')
                    synonym=input(f'\t\tEnter {self.__makeOrdinal(synCount)} synonym for {keyword}: ').strip().lower()
                    if synonym=='2' or (synCount>1 and synonym=='1'):
                        break 
                    synInvalid=self.__synIsInvalid(keyword,synonym,synList)
                if synonym=='1':
                    break #break to start adding keyword 
                elif synonym=='2':
                    self.__mainMenu()
                #add synonym to list
                synList.append(synonym)
                synCount+=1 
            #all done, add keyword and synonym pair
            thesaurus.addKeySynPair(keyword,synList)
            print(f"\tSuccessfully added {keyword} with following synonyms:")
            for syn in synList:
                print(f'\t\t{syn}')
            input('Press enter to continue...')
            #pop twice
            menuStack.pop()
            menuStack.pop()
            self.__editThesaurusMenu()


        def addSynonym():
            menuStack.push('Add Synonym')
            self.__printStack()
            print("\tExisting Keywords:")
            keywordList=thesaurus.getKeywords()
            for x in keywordList:
                print(f'\t{x}')
            print('\t(Type 1 to quit)')
            keyword=input('\tEnter keyword you want to add to: ')
            if keyword=='1':
                menuStack.pop()
                menuStack.pop()
                self.__editThesaurusMenu()
            elif keyword not in keywordList:
                print('\tKeyword does not exist!')
                input('\tPress enter to continue...')
                menuStack.pop()
                addSynonym()
            else:
                synList=[]
                synCount=1
                while True:
                    synInvalid=True
                    while synInvalid:
                        if synCount>1: #if not first 1st synonym, allow to finish keyword
                            print('\t\t(Type 1 if done with this keyword, type 2 to quit)')
                        else: 
                            print('\t\t(Type 2 to quit)')
                        synonym=input(f'\t\tEnter {self.__makeOrdinal(synCount)} synonym for {keyword}: ').strip().lower()
                        if synonym=='2' or (synCount>1 and synonym=='1'):
                            break
                        synInvalid=self.__synIsInvalid(keyword,synonym,synList)
                    if synonym=='1':
                        break 
                    elif synonym=='2':
                        self.__mainMenu()
                    #add synonym 
                    synList.append(synonym)
                    synCount+=1
                #all done, add synonyms
                thesaurus.addSynToKey(keyword,synList)
                print(f"\tSuccessfully added synonyms to '{keyword}'!")
                input("\tPress enter to continue...")
                self.__mainMenu()
        
        def removeKeyword():
            menuStack.push('Remove Keyword')
            self.__printStack()
            print("\tExisting Keywords:")
            keywordList=thesaurus.getKeywords()
            for x in keywordList:
                print(f'\t{x}')
            print('\n\t(Type 1 to quit)')
            keyword=input('\tEnter keyword you want to remove: ').strip().lower()
            if keyword=='1':
                menuStack.pop()
                menuStack.pop()
                self.__editThesaurusMenu()
            elif keyword not in keywordList:
                print('\tKeyword does not exist!')
                input('\tPress enter to continue...')
                menuStack.pop()
                removeKeyword()
            else:
                while True:
                    confirm=input(f"\t\tAre you sure you want to remove '{keyword}' and all it's synonyms? y/n: ").strip().lower()
                    if confirm=='y':
                        thesaurus.removeKeyword(keyword)
                        print(f"Successfully removed '{keyword}' and it's synonyms!")
                        input("Press enter to continue...")
                        menuStack.pop()
                        menuStack.pop()
                        self.__editThesaurusMenu()
                    elif confirm=='n':
                        menuStack.pop()
                        menuStack.pop()
                        self.__editThesaurusMenu()
                    else:
                        print('Invalid answer please try again!')
                        input('Press enter to continue...')
                        

        editMenuList = [
            ['Add Keyword with Synonyms',addKeyword],
            ['Add Synonyms to Keyword',addSynonym],
            ['Remove Keyword with Synonyms',removeKeyword],
            ['Back to Main Menu', self.__mainMenu],
        ]
        menuStack.push('Edit Thesaurus')
        self.__printStack()
        self.__printMenu(editMenuList)