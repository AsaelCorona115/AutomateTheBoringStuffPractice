'''

The following program is going to pick all the .txt files and move them into a 
new folder called SampleTexts.

'''
import os, zipfile, re, shutil
from pathlib import Path
from humre import *


#Getting the current folder
currentFolder = Path.cwd()




def selectiveMover(folder):
    
    newFolder = "copiedData"
    (currentFolder / newFolder).mkdir(exist_ok = True)
    
    print('Working...')
    #I wanted to use this folder but since I am using git it contains a bunch of hidden 
    #folders that I don't want to use so I will make a regex expression to skip them
    gitExpression = at_least(1, ".git")
    gitMatcher = re.compile(gitExpression)
    
    #This regex expression searches if the file is a .txt file
    textExpression = group('.txt')
    txtMatcher = re.compile(textExpression)

    for folder, subfolder, fileName in os.walk(folder):


        if gitMatcher.search(folder) != None:
            break
        
        else:
            for f in fileName:
                if txtMatcher.search(f) != None:
                    shutil.copy(folder + "\\" + f, newFolder)
                    
    
    print('Done')
    return

selectiveMover(currentFolder)