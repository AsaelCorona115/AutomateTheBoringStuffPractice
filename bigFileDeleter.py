'''
The following program scans the current directory for files bigger than 100MB and returns their 
paths as a list of strings

'''
import os, re
from pathlib import Path
from humre import *


currentDirectory = Path.cwd()

def bigFiles():

    results = []
    #

    for folder, subfolders, fileName in os.walk(currentDirectory):

        #Little regex expression to skip .git folder
        gitExpression = group('.git')
        gitMatcher = re.compile(gitExpression)
        gitResult = gitMatcher.search(folder)


        
        if gitResult != None:
            break
        

        #Getting the sizes of the files in the subfolders
        for s in subfolders:
            if s != ".git":
                folderPath = Path(folder) / s
                for insideFolders, insideSubfolders, insideFileName in os.walk(folderPath):
                    for insideF in insideFileName:

                        insideFilePath = Path(folderPath) / insideF
                        if os.path.getsize(insideFilePath) >= 10 ** 8:
                            results.append(insideFilePath)
                        
                    

        #Getting the sizes of the files at the root folder
        for f in fileName:
            filePath = Path(folder) / f
            if os.path.getsize(f) >= 10 ** 8:
                results.append(filePath)
        


        print("Big files Found: ")
        if len(results) == 0:
            print("None")
        else:
            for r in results:
                print(r)
       
    return


bigFiles()