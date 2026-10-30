print("ALPHABETIC PATTERS")

# each and every character is internally represented as integers, these integer representation is called as ASCII values

#The extended version of ascii value is values are called as unicode values

#ASCII values have standard of 256 characters ranging 0 to 255


# ' ' (space) --> 32
# '0' to '9' --> 48 - 57
# A - Z --> 65 - 90
# a - z --> 97 - 122


print("Conversion of charter to ordinal visa versa")
print("Ordinal function() ..")
#it returns the integer representational of the provided single character
#Syntax:-
#    ord(single_character)
#Note single character can be passed in the ord() function it will not take a string it will take character

print("Character function()")
#it returns character representation of the provided whole number  and negative and decimal are not allowed
#Syntax:-  chr(whole_number)


print("Examples:-")
print(ord('a'))
#print(ord('99')) only a single character allowed

print("Logic")
# Uppercase --> chr(64+val)
#Lowercase --->chr(96+val)