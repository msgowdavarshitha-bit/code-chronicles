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

def isAnagram(s1,s2):
    s1=strFilter(s1)
    s2=strFilter(s2)
    if len(s1)!=len(s2):
        return False
    else:
        dict={}
    for i in range(0,len(s2)):
        #for s1
        if s1[i] in dict:
            dict[s1[i]]=dict[s1[i]]+1
        else:
            dict[s1[i]]=+1

        #for s2
        if s2[i] in dict:
            dict[s2[i]]=dict[s2[i]]-1
        else:
            dict[s2[i]]=-1

    for key,val in dict.items():
        if val!=0:
            return False
    return True

s1=input("enter the string: ")
s2=input("ENter the string 2: ")
# result=isPangram(s)
if isAnagram(s1,s2):
    print("It is a anagram")
else:
    print("It is not a anagram")