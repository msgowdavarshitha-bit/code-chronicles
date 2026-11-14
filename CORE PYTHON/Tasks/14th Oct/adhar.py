str="123456789012"
print(str[:4])
print(str[4:8])
print(str[8:])
print(str[:4]+'-'+str[4:8]+'-'+str[8:])


for i in range(0,len(str),4):
    result=str[i:i+4]

    if i+4<len(str):
        print(result,end="-")
    else:
        print(result)