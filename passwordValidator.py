'''

re module is used for RegEx 
humre helps make it easier

'''

import re
from humre import *


def passWordValidator(password):
    
    #Checking first that the password is at least 8 characters long
    minimumLengthRegexExpression = at_least(8,DIGIT)
    lengthPattern = re.compile(minimumLengthRegexExpression)
    '''lengthValidator = lengthPattern.search(password)
    if lengthValidator == None:
        print("Invalid Password :c")
        return'''

    #TODO contain both uppercase and lowercase characters
    
    
    
    
    #TODO have at least one digit
    
    
    
    print("Valid Password :D")
    return 




while True:
    
    userInput= input("Please enter a Password :D \n")
    print("Enter Taco to exit")
    if user
    passWordValidator(userInput)