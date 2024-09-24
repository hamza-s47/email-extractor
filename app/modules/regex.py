import re

emailRegex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+ # username
    @ # @ symbol
    [a-zA-Z0-9.-]+ # domain name
    (\.[a-zA-Z]{2,4}) # dot-something
)''', re.VERBOSE)



def email_extract(text:str):
    matches = []
    for groups in emailRegex.findall(text):
        matches.append(groups[0])
    
    return matches