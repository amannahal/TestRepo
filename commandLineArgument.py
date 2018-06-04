from sys import argv
# read the WYSS section for how to run this
dict={}
commandLineStr=' '.join(argv[1:]).split(" ")
#print(commandLineStr)
for str in commandLineStr:
    #print(str)
    if(str.lower()in dict):
        dict[str.lower()]+=1
    else:
        dict[str.lower()]=1
print(dict)  
'''Your task in this exercise is as follows: 
a. Generate a string with N opening brackets ("[") and N closing brackets ("]"), in some arbitrary order. 
b. Determine whether the generated string is balanced; that is, whether it consists entirely of pairs of opening/closing brackets (in that order), none of which mis-nest. 
Examples: 
   []        OK   ][        NOT OK
   [][]      OK   ][][      NOT OK
   [[][]]    OK   []][[]    NOT OK'''