import os
import sys

currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

import DiffPriv.enc as enc

def test_rcipher ():
    assert enc.reverse_cipher('Test string') == 'gnirts tseT'

def test_lfl ():
    assert enc.lfl('Text', [['t', 'h'], ['e', 'i'], ['x', 'g'], ['T', 'H']]) == 'High'

def test_dlfl ():
    assert enc.dec_lfl('High', [['t', 'h'], ['e', 'i'], ['x', 'g'], ['T', 'H']]) == 'Text'

class TestPorta:
    def test_enc (self):
        cipher = enc.Porta()

        assert cipher.encrypt('DEFEND THE EAST WALL', 'War') == 'SRXTAV GZT WPFB JSNY'
    
    def test_dec (self):
        cipher = enc.Porta()

        assert cipher.encrypt('SRXTAV GZT WPFB JSNY', 'War') == 'DEFEND THE EAST WALL'