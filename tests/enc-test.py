import os
import sys

currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

import DiffPriv.enc as enc

def test_rcipher ():
    assert enc.reverse_cipher('Test string') == 'gnirts tseT'