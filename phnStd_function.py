#--Shaker Sami data engineer [shaker.samiy@gmail.com] [+201036497664  - +201119396597]
#------------------- Standariziation function ------------
"""
    This fucntion aims to get a number for user and check if it is an 11 digit
      and the country code is Egypt , 
      then the output will be in the standard format
      ex: number = 01119396597, country = eg , the standard number = +201119396507
"""

def phoneStd():
    number= input("Please insert the number \n")   
    if number.isdigit():
        print("Well done, valid input")
        #check length
        if len(number)==11:
            print("Your number is 11 digits")
            country= input("\n plese enter the coutry name, or coutry code, or first two letter of your coutry")
            if country in ("Eg","EG","Egypt","EGYPT", "مصر"):
                print("Welcome sir, Your standard number is: ", "+20",number)
            else:
                print("Your country not regoize in our system")
        else:
            print("The length of your number is not valid")
         
    else:
        print("Sorry you entered invalid number")
    while True:
        phoneStd()
phoneStd()

"""
Test case:
    case1:Fail
        number=123 -->length is not valid
    case2:Fail
        number=qw -->invalid number
    case3:Fail
        number=12345678911 -->valid
        country= rt        -->invalid
    case4:sccuess
        number=01036947664 -->valid
        country=Egypt      -->valid
        final output
        +201036497664
"""