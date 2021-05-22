import os
import sys
import csv

currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

import DiffPriv as diff

data = 314159265358979  # happy pi day!
pairs = [
(2, 20220),
(0, 314),
(-3, 71855),
(-2, 13856),
(-1, 1041),
(1, 2075),
]


def test_encryption():
    
    System = diff.enc.SSS(data)
    silence = False
    shares = System.divide(5, quiet=silence)
    encrypted = System.encrypt(width=5, quiet=silence)
    
    assert shares == [314, 159, 265, 358, 979]

def test_decryption():
    decrypted = diff.enc.dec_SSS(pairs)
