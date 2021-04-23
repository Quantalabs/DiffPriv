def reverse_cipher(msg: str):
    '''
    The reverse cipher. Note: this encryption scheme is not recommeneded, and is often reffered to as the 'weakest cipher ever in history.' Returns the string backwards.

        reverse_cipher(msg: str)

    PARAMETERS
    =================
    
    - msg: The message to encrypt with the reverse cipher
    '''
    return msg[::-1]