'''

re module is used for RegEx 
humre helps make it easier to read

'''

import re
from humre import *

def regexStrip(text, deletable=None ):
    
    print("Original string: " + text)
    #Code to execute if no second argument is passed
    if deletable == None:


        #Checking for white space at the beginning of the string 
        startPattern = at_least(1, WHITESPACE) + one_or_more(NONWHITESPACE)
        patternMatcherBeginning = re.compile(startPattern)
        whiteSpaceDetectorBeginning = patternMatcherBeginning.search(text)
        

        #Deleting white space at the beginning
        while whiteSpaceDetectorBeginning != None:
            text = text[1:]
            whiteSpaceDetectorBeginning = patternMatcherBeginning.search(text)


        #Checking for white space at the end of the string 
        endPattern = one_or_more(NONWHITESPACE) + at_least(1, WHITESPACE)
        patternMatcherEnd = re.compile(endPattern)
        whiteSpaceDetectorEnd = patternMatcherEnd.search(text)


        #Deleting white space at the end
        while whiteSpaceDetectorEnd != None:
            text = text[:-1]
            whiteSpaceDetectorEnd = patternMatcherEnd.search(text)
        
        print(" Result :D " + text)
    
    else:

        for c in deletable:
            regexPattern = one_or_more(c)
            patternMatcher = re.compile(regexPattern)
            deleter = patternMatcher.search(text)
            

            while deleter != None:
                text = text[0 : deleter.span()[0]] + text[deleter.span()[1]:]
                deleter = patternMatcher.search(text)
                
          
        print(" Result :D " + text)
    
    return 


regexStrip('The Dark Knight Rises', "aD")