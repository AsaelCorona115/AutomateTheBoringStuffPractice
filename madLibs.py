'''
    MODULES USED IN THIS PROGRAM:
    Pathlib : To interact with files in the hard drive
    os: To get paths 
    humre: Makes it easier to read Regex
    re: allows me to create patterns to search the text

'''
from pathlib import Path
from humre import *
import re



def textReplacer(fileName):
    #Opening the file
    target = open(fileName)
    targetContent = target.read()
    target.close()


    #A list containing all the words we are going to replace
    placeholderWords = ['ADJECTIVE', 'NOUN', 'ADVERB', 'VERB']


    # Search each word

    #This loop will run for each word in the list above
    for w in placeholderWords:
        placeHolderFinder = re.search(w, targetContent)
        

        #The search method gives me the position of the first find in the string
        #The while loop makes it run again until every instance of that keyword is replaced
        while placeHolderFinder != None:
            newWord = input(w + " found! Please enter a " + w + " \n"    )


            #Stitching together the string using the information given by "search"
            targetContent = targetContent[:placeHolderFinder.span(0)[0]] + newWord + targetContent[placeHolderFinder.span(0)[1]:]
            


            #Restart the finder to check the condition on the while loop
            placeHolderFinder = re.search(w, targetContent)
        
    
    #Printing the new text
    print(targetContent)


    
    #Writing the new file under a new name
    with open("newFile.txt", "w", encoding="UTF-8") as newFile:
        newFile.write(targetContent)    

#Calling the function
textReplacer('sample.txt')