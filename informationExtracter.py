'''
    pyperclip module allows me to copy and paste from and to the clipboard
    re module is used to create RegEx to find patterns in text
'''
import pyperclip, re 

#Getting the copied text from the clipboard
clipboardText = str(pyperclip.paste())

#Main function
def informationExtracter(text): 

    #Creating an empty list where we will store our matches
    matches = []
    '''TODO:
        *Format the result nicely :D
    '''

    #Phone Numbers RegEx expression  
    phone_re = re.compile(r'''
        
        (
                          
            (\d{3}|\(\d{3}\))?  # Area code
            (\s|-|\.)?  # Separator
            (\d{3})  # First three digits
            (\s|-|\.)  # Separator
            (\d{4})  # Last four digits
            (\s*(ext|x|ext\.)\s*(\d{2,5}))?  # Extension
        
        )''', re.VERBOSE)

    #Email RegEx Expression
    email_re = re.compile(r'''
    
    (
                          
        [a-zA-Z0-9._%+-]+  # Username
        @  # @ symbol
        [a-zA-Z0-9.-]+  # Domain name
        (\.[a-zA-Z]{2,4})  # Dot-something
                          
    )''', re.VERBOSE)


    #Making the created phoneMatcher interact with the text from the clipboard
    for groups in phone_re.findall(text):
        phone_num = '-'.join([groups[1], groups[3], groups[5]])
        if groups[6] != '':
            phone_num += ' x' + groups[6]
        matches.append(phone_num)
    
    #Making the created emailMatcher interact with the text from the clipboard
    for groups in email_re.findall(text):
        matches.append(groups[0])
    
    #Making the list into a single string to send it to the clipboard
    #Checking that there are matches
    if len(matches) > 0:
        pyperclip.copy('\n'.join(matches))
        print('Copied to clipboard:')
        print('\n'.join(matches))
    else:
        print('No phone numbers or email addresses found.')


    return




informationExtracter(clipboardText)