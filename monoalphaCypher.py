import string

ls = list(string.ascii_lowercase)
alphabet = list(string.ascii_lowercase)

key = alphabet
key.reverse()

print(ls)
print("key: ", key)

msg = input()
cypherText = ""

def cypher(): 
    global cypherText  
    for i in msg:
        if i != " ":
            cypherText += key[ls.index(i)]
        else:
            cypherText += " "
    print("cypher: ", cypherText)
    decyp(cypherText)  

def decyp(cypher):
    plaintext = ""
    for i in cypher:
        if i != " ":
            plaintext += ls[key.index(i)]
        else:
            plaintext += " "
    print("plaintext: ", plaintext)

cypher()  