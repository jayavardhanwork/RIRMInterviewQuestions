import re


def isValid(s):



    Pattern = re.compile("^\+?\(?([0-9]{3})\)?[-. ]?([0-9]{3})[-. ]?([0-9]{4})$")
    return Pattern.match(s)

str = input("Enter a phone number: ")
if (isValid(str)):
    print ("Valid Number")
else :
    print ("Invalid Number")
