def reverse_cipher(msg: str):
    '''
    The reverse cipher. Note: this encryption scheme is not recommeneded, and is often reffered to as the 'weakest cipher ever in history.' Returns the string backwards.

        reverse_cipher(msg: str)

    PARAMETERS
    =================
    
    - msg: The message to encrypt with the reverse cipher
    '''
    return msg[::-1] # pragma: no cover
    # Ignore coverage for the above due to a error with coverage.py that causes line 12 to be excluded from coverage and lower code coverage for the file.
