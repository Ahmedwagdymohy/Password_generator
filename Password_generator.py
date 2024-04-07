import string
import secrets


#checking if the password contains upperCharacters
def containUpper( password: str) -> bool:
    #checing every char in the password
    for char in password:
        if char.upper():
            return True
        
    return False

 #checking for the symbols in the password 
      
def containSymbol( password: str ) -> bool:
    #checking fir every char in the password whether it's a symbol or not
    for char in password:
        if string.punctuation:
            return True
        
    return False



def generatePassword( length : int, symbols: bool,  uppercase: bool):
    #creating the combination variable
    combination: str = string.ascii_lowercase + string.ascii_uppercase
    if symbols:
        combination += string.punctuation
    if uppercase:
        combination+= string.ascii_lowercase

    #getting the length of the combination
    combination_length = len (combination)       
    new_password : str= ''
    for _ in range(length):
        #generates a random value between the range given and then add it to the password
        new_password += combination[secrets.randbelow(combination_length)]
    return new_password

#
if __name__ == '__main__':
    new_pass: str = generatePassword(20,True ,True)
    print(new_pass)


