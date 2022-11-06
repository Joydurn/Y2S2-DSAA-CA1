
class Thesaurus: 
    def __init__(self):
        self.dict={}

    def createNew(self):
        #check if dictionary exists already
        if len(self.dict)!=0:
            print('\tWARNING: A thesaurus is already loaded, proceeding will delete the previous thesaurus (unless it was already saved)')
            answer=input('\tProceed? (y/n): ')
            while True:
                if answer=='y':
                    break #proceed to create
                elif answer=='n':
                    print('\tGoing back to main menu...')
                    return
                else:
                    print('\tInvalid answer, try again... \n')

        #refresh dictionary
        self.dict={}
        keyword,synList = self.getKeySynPair()
        if keyword==None and synList==None:
            return
        self.dict.update({keyword: synList})
        while True:
            answer=input('\tDo you want to add another keyword? (y/n): ').strip().lower()
            if answer=='y':
                keyword,synList=self.getKeySynPair()
                self.dict.update({keyword: synList})
            elif answer=='n':
                print('Your new Thesaurus is ready! Here it is...')
                self.printThesaurus()
                return
            else:
                print('\tInvalid answer, try again... \n')
        

    def getKeySynPair(self):
        #get keyword
        keyInvalid=True 
        while keyInvalid:
            keyword=input('\tEnter a keyword: ').strip().lower() 
            keyInvalid=self.keyIsInvalid(keyword)
        #now get synonyms
        synList=[]
        while True: #while not done entering synonyms: 
            #check if valid 
            synInvalid=True
            while synInvalid:
                print('\t\t(Type 1 if done with this keyword, type 2 to quit)')
                synonym=input(f'\t\tEnter a synonym for {keyword}: ').strip().lower() 
                if synonym in ['1','2']:
                    break
                synInvalid=self.synIsInvalid(synonym,synList)
            if synonym=='1':
                break 
            elif synonym=='2':
                return [None,None]
            #add synonym 
            synList.append(synonym)
        return (keyword,synList) #return as tuple

    #function to check if keys are valid
    def keyIsInvalid(self,keyword):
        if keyword in self.dict:
            print('\tKeyword already exists, please try again...')
            return True
        elif keyword in self.dict.values():
            print('\tKeyword already exists as a synonym, please try again...')
            return True
        elif not keyword.isalpha(): #check if has numbers/symbols
            print('\tOnly letters allowed, no numbers,symbols or spaces, try again')
            return True
        else:
            return False

    #TO DO: maybe automatiically add keyword to another thesaurus if synonym exists in another one 
    #function to check if synonym is valid, more lenient than for keyword
    def synIsInvalid(self,synonym,synList):
        if synonym in synList: #if was already entered
            print('\t\tSynonym already entered, please try again...')
            return True
        elif not synonym.isalpha(): #check if has numbers/symbols
            print('\t\tOnly letters allowed, no numbers or symbols, try again')
            return True
        else:
            return False

    def printThesaurus(self):
        print('Printing Thesaurus now:')
        print(self.dict)
        input('Press enter to continue...\n')