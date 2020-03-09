# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 20:47:42 2020

@author: Tj
"""

def encrypt(plaintext,key):
    ''' Encrypts a file Given a key and returns the ciphertext'''
    #Keypass is storing the bytes of key
    keypass = readfile(key)
    
    #Storing bytes of the plaintext
    toencrypt = readfile(plaintext)
    
    #initialize counters for loop
    keypasscount = 0
    dictcount = 0
    
    #mapping dictionary initialize
    keydict = {}
    
 
    #Mapping the key values to the ordered values
    while(not dictcount > 255):
        (keydict[str(dictcount)]) = (keypass[keypasscount])
        dictcount = dictcount + 1
        keypasscount = keypasscount + 1
 
    print('Encrypt Keydict \n\n\n\n')
    print(keydict)
    print('\n\n\n\n')
    

    #Creating the ciphertext and initializing it
    ciphertext = ''
    
    
    #Now that it is mapped, Gotta figure out a way to apply it to the plaintext
    for j in range(len(toencrypt)):
        ciphertext = ciphertext + keydict[toencrypt[j]] + ' '
    print('Cipher text\n\n\n\n')
    print(ciphertext + '\n\n\n\n')
    
   
    

  
    # Now, we have encrypted the plain text and returned the ciphertext
  #  print ('ciphertextbytes \n\n\n\n')
   # print (ciphertextbytes)
    #print ('\n\n\n\n')
    return ciphertext


def decrypt(ciphertext,key):
    '''Decrypts a file using a given key and returns the plaintext'''
    
    #For decryption, You can see it as reversing the encryption dictionary. 
    #for example, if the value is 1 mapped to 8; dictionary[1]  = 8, t
    #then the other way around, it means 8 is mapped to 1. So lets reverse dictionary
    
    decryptdict = {}
    keypasscount = 0
    
    keypass = readfile(key)
    
    #Mapping the dictionary  in reverse order
    while(not keypasscount > 255):
        decryptdict[keypass[keypasscount]] = str(keypasscount)
    
        
        
        #keypass[keypasscount] = decryptdict[str(dictcount)]
        keypasscount += 1
        
    print('HERE IS THE CIPHERTEXT!!!!!!!!!!!!!!')
    
    todecrypt = readfile(ciphertext)
   
    print('decryptdict \n\n\n\n') 
    print(decryptdict)
    print('\n\n\n\n')
    
    plaintext = ''
    
    for x in range (len(todecrypt)):
        plaintext = plaintext + decryptdict[todecrypt[x]] + ' ' 
    
    print('plaintext \n\n\n\n')
    print(plaintext)
    return plaintext
        
    




def readfile(s):
    '''reads contents of a file (binary) and returns a string list of the bytes'''
    namehandle = open(s,'rb')
    
    bindata = namehandle.read()
    namehandle.close()
    listofbytes = []
    
    for byte in bindata:
        listofbytes.append(str(byte))
       
    
    print('listofbytes \n\n\n\n')
    print(listofbytes)
    print('\n\n\n\n ----------------------------------------------------------------------')
    return listofbytes
    
    
    
        

def writefile(filename,content):
    '''Writes to a binary file by taking a string input and converting that to binary'''
    file = open(filename,'wb')
    bytecontent = bytes(content,'utf-8')
    file.write(bytecontent)
    print('i just wrote \n\n\n\n')
    file.close()
    
    
    
    


