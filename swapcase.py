## this is how we can convert each character from lower case to upper case and upper case to lower case 
def swap_case(s):
    ## first, we should assign a new_string to cast each character
    new_string= ''
    for character in s:
        if character.isalpha() and character.isupper():
            new_string+= character.lower()
        elif character.isalpha() and character.islower():
            new_string+= character.upper()
        else:
            new_string+= character
        
    return new_string