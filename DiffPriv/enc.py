def reverse_cipher(msg: str):
    '''
    The reverse cipher. Note: this encryption scheme is not recommeneded, and is often reffered to as the 'weakest cipher ever in history.' Returns the string backwards.

    

        reverse_cipher('Hi') # Returns 'iH'

    ## Parameters
    
    - msg: The message to encrypt with the reverse cipher
    '''
    return msg[::-1] # pragma: no cover

def lfl(text: str, key: list):
    '''
    Does a letter for letter encryption. Takes one letter and replaces it with another letter specified in the key.
    
    

        lfl('Text', [['t', 'h'], ['e', 'i'], ['x', 'g'], ['T', 'H']]) # Returns 'High'. NOTE: this is case sensitive.
    
    ## Parameters

    - text: Text to encrypt

    - key: The encryption key. eg. `[['a', 'z'], ['b', 'y'], ..., ['y', 'b'], ['z', 'a']]` will change all a's to z's and b's to y's, etc.
    '''
    splittext = [char for char in text]
    newtext = []

    for x in range(0, len(splittext)):
        charfound = False
        for y in range(0, len(key)):
            if key[y][0] == splittext[x]:
                rchar = key[y][1]
                charfound = True
        
        if charfound is True:
            newtext.append(rchar)
        else:
            newtext.append(splittext[x])

    return ''.join(newtext)

def dec_lfl(text: str, key: list):
    '''
    Decrypts a letter for letter encryption.
    
    

        dec_lfl('High', [['t', 'h'], ['e', 'i'], ['x', 'g'], ['T', 'H']]) # Returns 'Text'. NOTE: this is case sensitive.
    
    ## Parameters

    - text: Text to encrypt

    - key: The encryption key. eg. `[['a', 'z'], ['b', 'y'], ..., ['y', 'b'], ['z', 'a']]` will change all z's to a's and y's to b's, etc.
    '''
    splittext = [char for char in text]
    newtext = []

    for x in range(0, len(splittext)):
        charfound = False
        for y in range(0, len(key)):
            if key[y][1] == splittext[x]:
                rchar = key[y][0]
                charfound = True
        
        if charfound is True:
            newtext.append(rchar)
        else:
            newtext.append(splittext[x])

    return ''.join(newtext)

class Porta:
    def __init__(self, alphabet=None):
        """
        For using the Porta Cipher. Read about the cipher - [http://practicalcryptography.com/ciphers/classical-era/porta/](http://practicalcryptography.com/ciphers/classical-era/porta/)

        

            cipher = Porta(alphabet=None) 
        
        ## Parameters

        `alphabet`: Defaults to none. The alphabet for the porta cipher
        """
        if alphabet is None:
            self.alphabet = {
                "A": ("ABCDEFGHIJKLM ", "NOPQRSTUVWXYZ "),
                "B": ("ABCDEFGHIJKLM ", "NOPQRSTUVWXYZ "),
                "C": ("ABCDEFGHIJKLM ", "ZNOPQRSTUVWXY "),
                "D": ("ABCDEFGHIJKLM ", "ZNOPQRSTUVWXY "),
                "E": ("ABCDEFGHIJKLM ", "YZNOPQRSTUVWX "),
                "F": ("ABCDEFGHIJKLM ", "YZNOPQRSTUVWX "),
                "G": ("ABCDEFGHIJKLM ", "XYZNOPQRSTUVW "),
                "H": ("ABCDEFGHIJKLM ", "XYZNOPQRSTUVW "),
                "I": ("ABCDEFGHIJKLM ", "WXYZNOPQRSTUV "),
                "J": ("ABCDEFGHIJKLM ", "WXYZNOPQRSTUV "),
                "K": ("ABCDEFGHIJKLM ", "VWXYZNOPQRSTU "),
                "L": ("ABCDEFGHIJKLM ", "VWXYZNOPQRSTU "),
                "M": ("ABCDEFGHIJKLM ", "UVWXYZNOPQRST "),
                "N": ("ABCDEFGHIJKLM ", "UVWXYZNOPQRST "),
                "O": ("ABCDEFGHIJKLM ", "TUVWXYZNOPQRS "),
                "P": ("ABCDEFGHIJKLM ", "TUVWXYZNOPQRS "),
                "Q": ("ABCDEFGHIJKLM ", "STUVWXYZNOPQR "),
                "R": ("ABCDEFGHIJKLM ", "STUVWXYZNOPQR "),
                "S": ("ABCDEFGHIJKLM ", "RSTUVWXYZNOPQ "),
                "T": ("ABCDEFGHIJKLM ", "RSTUVWXYZNOPQ "),
                "U": ("ABCDEFGHIJKLM ", "QRSTUVWXYZNOP "),
                "V": ("ABCDEFGHIJKLM ", "QRSTUVWXYZNOP "),
                "W": ("ABCDEFGHIJKLM ", "PQRSTUVWXYZNO "),
                "X": ("ABCDEFGHIJKLM ", "PQRSTUVWXYZNO "),
                "Y": ("ABCDEFGHIJKLM ", "OPQRSTUVWXYZN "),
                "Z": ("ABCDEFGHIJKLM ", "OPQRSTUVWXYZN "),
            }
        else:
            self.alphabet = alphabet

    def encrypt(self, text: str, key: str):
        """
        Encrypts text using the porta cipher.

        

            cipher = Porta()
            cipher.encrypt(text: str, key: str)
        
        ## Parameters

        text: `str` The text to encrypt (will only encrypt characters A-M and no numbers or symbols, and simply doesn't change the characters.)

        key: `str` The key to encrypt with
        """
        brokenkey = list(key.upper())
        brokentext = list(text.upper())
        key1 = []

        for charpos in range(0, len(brokentext)):
            if charpos >= len(brokenkey):
                brokenkey = brokenkey+brokenkey
                key1.append(brokenkey[charpos])
            else:
                key1.append(brokenkey[charpos])

        encrypted = []

        table = [self.alphabet[char.upper()] for char in key1]
        
        for x in range(0, len(brokentext)):
            found = False
            for char in range(0, len(list(table[x][0]))):
                if list(table[x][0])[char] == brokentext[x]:
                    encrypted.append(list(table[x][1])[char])
                    found = True
                    break
                elif list(table[x][1])[char] == brokentext[x]:
                    encrypted.append(list(table[x][0])[char])
                    found = True
                    break

            if found is False:
                encrypted.append(brokentext[x])
            


        return ''.join(encrypted)

    def decrypt(self, text: str, key: str):
        """
        Decrypts text using the porta cipher.

        

            cipher = Porta()
            cipher.decrypt(text: str, key: str)
        
        ## Parameters

        text: `str` The text to decrypt

        key: `str` The key to decrypt with
        """

        brokenkey = list(key.upper())
        brokentext = list(text.upper())
        key1 = []

        for charpos in range(0, len(brokentext)):
            if charpos >= len(brokenkey):
                brokenkey = brokenkey+brokenkey
                key1.append(brokenkey[charpos])
            else:
                key1.append(brokenkey[charpos])

        decrypted = []

        table = [self.alphabet[char.upper()] for char in key1]
        
        for x in range(0, len(brokentext)):
            found = False
            for char in range(0, len(list(table[x][0]))):
                if list(table[x][1])[char] == brokentext[x]:
                    decrypted.append(list(table[x][0])[char])
                    found = True
                    break
                elif list(table[x][0])[char] == brokentext[x]:
                    decrypted.append(list(table[x][1])[char])
                    found = True
                    break
            
            if found is False:
                decrypted.append(brokentext[x])

        return ''.join(decrypted)
