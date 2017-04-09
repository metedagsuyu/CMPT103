#fix line 31
# name: Metehan Dagsuyu
# program: Lab2MD.py
#---------------------------

#Purpose: encrypt text
#Syntax: encrypt(old)
#Parameter: old: any unencrypted string
#Return value: new : encrypted value of the string
def encrypt(old):
    new = ""
    for i in range(len(old)):
        new += chr(ord(old[i])+i+5)
    return new

#Purpose: decrypt text
#Syntax: decrypt(old)
#Parameter: old: any encrypted string
#Return value: result: decrypted value of the string
def decrypt(old):
    result = ""
    for i in range(len(old)):
        result +=chr(ord(old[i])-i-5)
    return result


#Purpose: compress string
#Syntax: compress(string)
#Parameter: string: uncompressed string
#Return value: final : compressed version of the string
def compress(string): #"abc" returns 1a1b1c
    a = 0
    final = ""
    for i in range(len(string)):
        try:
            if string[i] == string[i+1]:
                a += 1
            else:
                final +=  string[i] + str(a+1)
                a = 0 
        except IndexError:
            final += string[i] + str(a+1)
            a = 0
    return final

#Purpose: expand string
#Syntax: expand(string)
#Parameter: string: compressed string
#Return value: final : expanded/uncompressed version of the string
def expand(string):
    
    
    return final

#optional bonus ,,, do it