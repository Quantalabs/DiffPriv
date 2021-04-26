def reverse_cipher(msg: str):
    '''
    The reverse cipher. Note: this encryption scheme is not recommeneded, and is often reffered to as the 'weakest cipher ever in history.' Returns the string backwards.

    .. code-block:: python

        reverse_cipher('Hi') # Returns 'iH'

    PARAMETERS
    ++++++++++++++
    
    - msg: The message to encrypt with the reverse cipher
    '''
    return msg[::-1] # pragma: no cover

def lfl(text: str, key: list):
    '''
    Does a letter for letter encryption. Takes one letter and replaces it with another letter specified in the key.
    
    .. code-block:: python

        lfl('Text', [['t', 'h'], ['e', 'i'], ['x', 'g'], ['T', 'H']]) # Returns 'High'. NOTE: this is case sensitive.
    
    PARAMETERS
    ++++++++++++++++++++

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
    
    .. code-block:: python

        dec_lfl('High', [['t', 'h'], ['e', 'i'], ['x', 'g'], ['T', 'H']]) # Returns 'Text'. NOTE: this is case sensitive.
    
    PARAMETERS
    ++++++++++++++++++++

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