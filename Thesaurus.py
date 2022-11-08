import random
class Thesaurus: 
    def __init__(self):
        # self.__fullList=[]
        self.__fullList=[
            ['sad',['depressed','down','bear','huge','momy']],
            ['happy',['daring','adequate','bold','bait','cold','bear','beautiful']]
        ]
    
    def __str__(self):
        return f'{self.__fullList}'

    def getStringFormat(self):
        fullList=self.getFullThesaurus()
        string=''
        sep=', '
        for keyword,synList in [sublist for sublist in fullList]:
            string+=f'{keyword}: '
            string+=sep.join(synList)
            string+='\n'
        return string

    #create new thesaurus from a multiline string (used when opening files)
    def createFromString(self,string):
        def addFromOneLineString(lineString):
            keyIndex=None
            #first find keyword
            for index,x in enumerate(lineString):
                if x==':':
                    keyIndex=index 
                    break
            keyword=lineString[0:keyIndex]
            synString=lineString[keyIndex+2:] #string of all synonyms
            #now find synonym list
            synList=[]
            newSynIndex=None
            lastIndex=0
            for index,x in enumerate(synString):
                if x==',': #if comma 
                    newSynIndex=index
                    synList.append(synString[lastIndex:newSynIndex]) #append new synonym
                    lastIndex=index+2 #new start index of next synonym 
                elif index==len(synString)-1: #if end of string
                    newSynIndex=index
                    synList.append(synString[lastIndex:newSynIndex+1]) #append new synonym
                    lastIndex=index+2 #new start index of next synonym 
            self.addKeySynPair(keyword,synList)
        self.__fullList=[]
        for line in string.splitlines(): #iterate through each line
            addFromOneLineString(line)
            
    
    def size(self):
        return len(self.__fullList)

    def getFullThesaurus(self):
        return self.__fullList

    def getKeywords(self):
        return [subList[0] for subList in self.__fullList]
    
    def getAllSynonyms(self):
        return [subList[1] for subList in self.__fullList]

    def getSynonyms(self,keyword):
        for subList in self.__fullList: 
            if subList[0]==keyword: 
                return subList[1]
    
    def addKeyword(self,keyword):
        self.__fullList.append([keyword,None])

    def addSynToKey(self,keyword,synList): #add to existing keyword
        for keyIndex,subList in enumerate(self.__fullList):
            if subList[0]==keyword:
                for synonym in synList:
                    self.__fullList[keyIndex][1].append(synonym)

    def addKeySynPair(self,keyword,synList):
        self.__fullList.append([keyword,synList])
    
    #refresh the thesaurus to empty 
    def refresh(self):
        self.__fullList=[]
    #*****************SORTING ALGORITHMS ***********************
    #sort alphabetically (quicksort)
    def sortAlphabetically(self):
        def __sort(symList): #actual algorithm used
            if len(symList) <=1:
                return symList
            else:
                pivot = symList.pop()

            items_greater = []
            items_lower = []

            for item in symList:
                if item > pivot:
                    items_greater.append(item)
                else:
                    items_lower.append(item)

            return __sort(items_lower) + [pivot] + __sort(items_greater)
        for keyIndex,subList in enumerate(self.__fullList): #sorting every synonym list
            symList=subList[1]
            self.__fullList[keyIndex][1]=__sort(symList)
            
    def sortKeywords(self): #only used when creating thesaurus
        def __sort(keySynPairList): #actual algorithm used
            if len(keySynPairList) <=1:
                return keySynPairList
            else:
                pivot = keySynPairList.pop()

            items_greater = []
            items_lower = []

            for item in keySynPairList:
                if item[0] > pivot[0]:
                    items_greater.append(item)
                else:
                    items_lower.append(item)

            return __sort(items_lower) + [pivot] + __sort(items_greater)
        self.__fullList=__sort(self.__fullList)

    #sort by length then alphabetically (quicksort)
    def sortLengthAlphabetically(self):
        #custom compare function to enable sorting by 2 keys
        def __compare(a, b):
            if len(a) != len(b):
                return len(a) > len(b)
            else:
                return a > b
        def __sort(symList):
            if len(symList) <=1:
                return symList
            else:
                pivot = symList.pop()

            items_greater = []
            items_lower = []

            for item in symList:
                if __compare(item,pivot):
                    items_greater.append(item)
                else:
                    items_lower.append(item)

            return __sort(items_lower) + [pivot] + __sort(items_greater)
        for keyIndex,subList in enumerate(self.__fullList): #sorting every synonym list
            symList=subList[1]
            self.__fullList[keyIndex][1]=__sort(symList)
    
    #sort by length then randomly (quicksort)
    def sortLengthRandomly(self):
        #custom compare function to enable sorting by 2 keys
        def __compare(a, b):
            if len(a) != len(b):
                return len(a) > len(b)
            else:
                #returns a random True or False value 
                #effectively returning either a>b or a<b for the random part of the sort
                return bool(random.getrandbits(1))
              
        def __sort(symList):
            if len(symList) <=1:
                return symList
            else:
                pivot = symList.pop()

            items_greater = []
            items_lower = []

            for item in symList:
                if __compare(item,pivot):
                    items_greater.append(item)
                else:
                    items_lower.append(item)

            return __sort(items_lower) + [pivot] + __sort(items_greater)
        for keyIndex,subList in enumerate(self.__fullList): #sorting every synonym list
            symList=subList[1]
            self.__fullList[keyIndex][1]=__sort(symList)

    def sortRandomly(self): #random sort
        def __sort(symList):
            if len(symList) <=1:
                return symList
            else:
                pivot = symList.pop()

            items_greater = []
            items_lower = []

            for item in symList:
                if bool(random.getrandbits(1)): #random true or false
                    items_greater.append(item)
                else:
                    items_lower.append(item)
            return __sort(items_lower) + [pivot] + __sort(items_greater)
        for keyIndex,subList in enumerate(self.__fullList): #sorting every synonym list
            symList=subList[1]
            self.__fullList[keyIndex][1]=__sort(symList)
     
    

    

    


    