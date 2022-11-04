
class Thesaurus: 
    def __init__(self):
        self.dict={}

    def createNew(self):
        #refresh dictionary
        self.dict={}
        keyword,synList = self.getKeySynPair()
        self.dict.update({keyword: synList})
        while True:
            answer=input('Do you want to add another keyword? (y/n): ').strip().lower()
            if answer=='y':
                keyword,synList=self.getKeySynPair()
                self.dict.update({keyword: synList})
            elif answer=='n':
                print('Your new Thesaurus is ready! Here it is...')
                self.printThesaurus()
                return
            else:
                print('Invalid answer, try again... \n')
        

    def getKeySynPair(self):
        #get keyword
        keyInvalid=True 
        while keyInvalid:
            keyword=input('Enter a keyword: ').strip().lower() 
            keyInvalid=self.keyIsInvalid(keyword)
        #now get synonyms
        synList=[]
        while True: #while not done entering synonyms: 
            #check if valid 
            synInvalid=True
            while synInvalid:
                print('(Type 1 if done, type 2 to quit)')
                synonym=input(f'Enter a synonym for {keyword}: ').strip().lower() 
                if synonym in ['1','2']:
                    break
                synInvalid=self.synIsInvalid(synonym,synList)
            if synonym=='1':
                break 
            elif synonym=='2':
                mainMenu()
            #add synonym 
            synList.append(synonym)
        return (keyword,synList) #return as tuple

    #function to check if keys are valid
    def keyIsInvalid(self,keyword):
        if keyword in self.dict:
            print('Keyword already exists, please try again...')
            return True
        elif keyword in self.dict.values():
            print('Keyword already exists as a synonym, please try again...')
            return True
        elif not keyword.isalpha(): #check if has numbers/symbols
            print('Only letters allowed, no numbers,symbols or spaces, try again')
            return True
        else:
            return False

    #TO DO: maybe automatiically add keyword to another thesaurus if synonym exists in another one 
    #function to check if synonym is valid, more lenient than for keyword
    def synIsInvalid(self,synonym,synList):
        if synonym in synList: #if was already entered
            print('Synonym already entered, please try again...')
            return True
        elif not synonym.isalpha(): #check if has numbers/symbols
            print('Only letters allowed, no numbers or symbols, try again')
            return True
        else:
            return False

    def printThesaurus(self):
        print('Printing Thesaurus now:')
        print(self.dict)
        input('Press enter to continue...\n')