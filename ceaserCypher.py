input = "string"
encoded=''
k=3

def encyp(encoded):
    print("------encrpted----------")
    for st in input:
     print(chr(ord(st)+3%26))
     encoded+= chr(ord(st)+3%26)
    
    decyp(encoded) 
    
    
print("original=",input)    
def decyp(encoded):
    print("------decrpted----------")
    for st in encoded:
     print(chr(ord(st)-3%26))
        
        
encyp(encoded)