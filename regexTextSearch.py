from pathlib import Path
import re
import os






#Main function
def regexSearch(targetWord):

    #A list where I'll store all the found instances, initialized empty
    instances = []



    textFiles = os.listdir('SampleTexts')
    for f in textFiles:

        #Creating the file path for each file
        path = Path(Path.cwd(), "SampleTexts", f )       

        #Getting the text 
        content = open(path, encoding='UTF-8')

        #Using the readlines method to get a list of each line in the text
        textContent = content.readlines()
        content.close()

        #Searching for the word in each line
        for l in textContent:

            isWordThere = re.search(targetWord, l)
            if isWordThere != None:
                instances.append(l)


        
        

    if instances != []:
        for l in instances:
            print(l)
    else:
        print("No matches found :c")
    return 







#Obtaining the word to search
wordToSearch = input("Enter Regex to Search \n ")


regexSearch(wordToSearch)




