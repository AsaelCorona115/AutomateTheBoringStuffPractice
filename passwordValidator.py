'''

re module is used for RegEx 
humre helps make it easier

'''

import re
from humre import *


def passWordValidator(password):
    
    #Checking first that the password is at least 8 characters long
    minimumLengthRegexExpression = at_least(8,ANYCHAR)
    lengthPattern = re.compile(minimumLengthRegexExpression)
    lengthValidator = lengthPattern.search(password)
    if lengthValidator == None:
        print("Sorry, not enough characters \n \n")
        return

    
    
    
    #Uppercase
    upperRegex = at_least(1, UPPERCASE)
    capitalPattern = re.compile(upperRegex)
    upperValidator = capitalPattern.search(password)
    if upperValidator == None:
        print("Password must have at least 1 uppercase letter \n \n")
        return
    

    #LowerCase
    lowerRegex = at_least(1, LOWERCASE)
    nonCapitalPattern = re.compile(lowerRegex)
    lowerValidator = nonCapitalPattern.search(password)
    if lowerValidator == None:
        print("Password must have at least 1 lowercase letter \n \n")
        return
    
    #At least one digit
    digitRegex = at_least(1, DIGIT)
    digitPattern = re.compile(digitRegex)
    digitValidator = digitPattern.search(password)
    if digitValidator == None:
        print("Password must have at least 1 digit \n \n")
        return
    
    
    print("Valid Password :D \n \n")
    return 



while True:
    
    
    
    print("CTRL-C to exit")
    userInput= input("Please enter a Password :D \n")
    
    if userInput == None:
        break
    
    passWordValidator(userInput)