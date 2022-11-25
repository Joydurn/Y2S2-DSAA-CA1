# Jayden Yap p2112790 DAAA/2B/04 DSAA CA1 thesaurus.py
#Implemented thesaurus class using a 3D list
#List vs linked list:
#Linked list: Faster insertion/deletion 
#List: Faster element lookup and sorting (at least for quicksort)
#Decided to use list because of all these operations, sorting is the one that takes the longest, so performance on average for any of these operations would be about the same on a list

import random
import re
class Thesaurus: 
    def __init__(self):
        self.__fullList=[]
        
    def __str__(self): #when printed, return the list
        return f'{self.__fullList}'

    #is the thesaurus empty?
    def isEmpty(self):
        if not self.__fullList:
            return True 
        else: 
            return False
    
    #returns the proper format for printing/saving the thesaurus
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
                elif not x.isalpha(): #if not alphabetic
                    raise Exception('Non-alphabetic detected')
            keyword=lineString[0:keyIndex]
            synString=lineString[keyIndex+2:] #string of all synonyms
            #now find synonym list
            synList=[]
            newSynIndex=None
            lastIndex=0
            nextIsSpace=False
            for index,x in enumerate(synString):
                if x==',': #if comma 
                    newSynIndex=index #end index of new synonym
                    synList.append(synString[lastIndex:newSynIndex]) #append new synonym
                    #check that next element is a space (otherwise error)
                    if synString[index+1]!=' ':
                        raise Exception('Invalid formatting1')
                    else:
                        lastIndex=index+2 #new start index of next synonym 
                        nextIsSpace=True
                elif x==' ' and not nextIsSpace:
                    raise Exception('Invalid formatting2')
                elif not x.isalpha() and x!=' ': #if x not letter or space, raise error 
                    raise Exception('Invalid formatting3')
                elif index==len(synString)-1: #if end of string
                    newSynIndex=index
                    word=synString[lastIndex:newSynIndex+1]
                    synList.append(word) #append new synonym

            self.addKeySynPair(keyword,synList)
        self.refresh()
        for line in string.splitlines(): #iterate through each line
            addFromOneLineString(line)
            #if returned here
            
    #return number of keywords
    def size(self):
        return len(self.__fullList)

    #simply returns full thesaurus
    def getFullThesaurus(self):
        return self.__fullList

    #return list of all keywords
    def getKeywords(self):
        return [subList[0] for subList in self.__fullList]
    
    #return list of sublists of synonyms
    def getAllSynonyms(self):
        return [subList[1] for subList in self.__fullList]

    #get a list of synonyms depending on keyword
    def getSynonyms(self,keyword):
        for subList in self.__fullList: 
            if subList[0]==keyword: 
                return subList[1]
    
    #add a keyword with no synonyms
    def addKeyword(self,keyword):
        if self.isInThesaurus(keyword):
            raise Exception('Keyword exists in thesaurus')
        self.__fullList.append([keyword,None])

    #return single list of every keyword/synonym (used for checking)
    def getWords(self):
        completeList=[]
        for keyword in self.getKeywords():
            completeList.append(keyword)
        for synList in self.getAllSynonyms():
            for syn in synList: 
                completeList.append(syn)
        return completeList 

    #check if word exists in thesaurus
    def isInThesaurus(self,word):
        completeList=self.getWords()
        if word in completeList:
            return True 
        else:
            return False

    #add one or more synonyms to a keyword
    def addSynToKey(self,keyword,synList): #add to existing keyword
        for keyIndex,subList in enumerate(self.__fullList):
            if subList[0]==keyword:
                for synonym in synList:
                    if self.isInThesaurus(synonym):
                        raise Exception('Synonym already in thesaurus')
                    self.__fullList[keyIndex][1].append(synonym)

    #add a keyword along with list of synonyms
    def addKeySynPair(self,keyword,synList):
        if self.isInThesaurus(keyword):
            raise Exception('Keyword is a duplicate')
        for syn in synList:
            if self.isInThesaurus(syn):
                raise Exception('Synonym is a duplicate')
        
        
        self.__fullList.append([keyword,synList])
    
    #remove a keyword along with synonyms
    def removeKeyword(self,keyword):
        for keyIndex,subList in enumerate(self.__fullList):
            if subList[0]==keyword:
                self.__fullList.pop(keyIndex)

    #refresh the thesaurus to empty 
    def refresh(self):
        self.__fullList=[]

    #*****************SORTING ALGORITHMS ***********************
    #only used when creating thesaurus and opening
    def sortKeywords(self): 
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
            if len(a) != len(b): #sort by length 
                return len(a) > len(b) 
            else:  #if same length, randomise
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
    
    #splits a string into different words, ignoring punctuations and spaces
    #used by a few functions
    def splitNonAlpha(self,s):  
            list=re.split('\W+', s)
            return list

    #takes a string and turns any word that matches a synonym into the corresponding keyword, returns new string
    def simplifyString(self,string):
        #check if a word is capitalised
        def isCapital(word):
            if len(word)>2:
                if word[0].isupper() and word[1:].islower():
                    return True 
                else: 
                    return False
            elif len(word)==2 and word[0].isupper() and word[1].islower():
                return True
            elif len(word)==1 and word.isupper():
                return True 
            else:
                return False
                
        newString=string
        wordsList=self.splitNonAlpha(newString) #get individual words
        #for every word in the string
        for word in wordsList:
            #check if word matches keyword
            for keyword,synList in [sublist for sublist in self.getFullThesaurus()]:
                #check if lowercase match
                if word.islower() and word in synList: 
                    newString=re.sub(fr"\b{word}\b",keyword, newString,count=1) #replace lowercase
                #check if uppercase match
                elif word.isupper() and word.lower() in synList:  
                    newString=re.sub(fr"\b{word}\b",keyword.upper(), newString,count=1) #replace uppercase
                #check if capitalised match
                elif isCapital(word) and word.lower() in synList: #check if capitalised
                    newString=re.sub(fr"\b{word}\b",keyword.title(), newString,count=1) #replace capitalised
        return newString

    #takes a string and turns any word that matches a keyword into a synonym, alternating the synonyms in order, returns new string
    def elegantString(self,string): #for elegant we must iterate through the synonyms too
        def getCountList(text):
            #get unique only 
            str_=text
            wordSet=set([word.lower() for word in self.splitNonAlpha(str_) if word !=''])
            countList=[]
            for word in wordSet: 
                countList.append(string.lower().count(word)) 
            return (wordSet,countList)

        def getOccurencesOfOneWord(wordsList,word):
            list=[]
            for x in wordsList:
                if x.lower()==word.lower():
                    list.append(x)
            return list
            
        newString=string
        wordSet,countList=getCountList(newString)
        wordList=self.splitNonAlpha(newString)
        #we use re.sub to replace instead of str.replace because it only replaces whole words, so it won't replace something that was previously replaced
        for keyword,synList in [sublist for sublist in self.getFullThesaurus()]:
            if keyword in wordSet:
                index=list(wordSet).index(keyword) #find index in wordSet for keyword

                if countList[index]>1: #if more than one occurence of this keyword in string
                    occurenceWords=getOccurencesOfOneWord(wordList,keyword) #get all occurences of keyword in string regardless of capitalisation
                    for count,occurence in enumerate(occurenceWords): #for every occurence of keyword
                        if count>=len(synList): #if not enough synonyms (more occurences than synonyms available)
                            count=0 #default to first synonym
                        #now check capitalisations
                        replacement=synList[count] #get next synonym to be used as replacement
                        if occurence.isupper(): #if uppercase
                            newString=re.sub(fr"\b{occurence}\b",replacement.upper(), newString,count=1) #replace uppercase
                        elif occurence[0].isupper() and occurence[1:].islower(): #if capitalised 
                            newString=re.sub(fr"\b{occurence}\b",replacement.title(), newString,count=1) #replace capitalised
                        else: #if mEssY capitalisation/or just lowercase
                            newString=re.sub(fr"\b{occurence}\b",replacement, newString,count=1) #replace lowercase
                else: #else only one occurence of keyword
                    newString=re.sub(fr"\b{keyword}\b",synList[0], newString,count=1)
                    # newString.replace(keyword,synList[0],1)
        return newString

    #EXTRA OPTION 1: Get synonyms for any word
    def findSynonymFromWord(self,string):
        #function to get random index excluding an index
        # def gen_random_number(low, high, exclude):
        #     return random.choice(
        #         [number for number in range(low, high)
        #         if number not in exclude]
        #     )

        word=string.lower()
        for keyword,synList in [sublist for sublist in self.__fullList]:
            if keyword==word:
                return synList #return random synonym
            elif word in synList:
                if len(synList)==1: #only one synonym
                    return [keyword]
                elif len(synList)==2:
                    index=synList.index(word)
                    if index==0:
                        result=[synList[1]]
                        result.insert(0,keyword)
                        return result
                    else:
                        result=[synList[0]]
                        result.insert(0,keyword)
                        return result
                else:
                    synList.remove(word)
                    synList.insert(0,keyword)
                    return synList #return any synonym that is not the input given
        
    



        



    

    


    