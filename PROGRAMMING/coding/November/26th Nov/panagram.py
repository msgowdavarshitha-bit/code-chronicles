print("pangrams: strings that includes all the 26 alphabets character is present in the string excepty special charaters such as casing,special symbols,characters and spaces")

#eg:-  s="9-9-Thelazyquick,768brownfox jumps over the lazy dog"

#step1:Filtration
# s="thelazyquickbrownfoxjumpsoverthelazydog" 
#dict={
#'t':2,
#'h':2}

def strFilter(s):
    nstr=""
    for i in s:
        if 'A'<=i<='Z':
            nstr+=chr(ord(i)+32)
        elif 'a'<=i<='z':
            nstr+=i
    return nstr

def isPangram(s):
    s=strFilter(s)
    if len(s)<26:
        return False
    dict={}
    for i in range(0,len(s)):
        if s[i] in dict:
            dict[s[i]]+=1
        else:
            dict[s[i]]=1

    print(dict)
    return len(dict)==26


s=input("enter the string")
# result=isPangram(s)
if isPangram(s):
    print("It is a pangram")
else:
    print("It is not a pangram")