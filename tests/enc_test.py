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
    assert enc.lfl('Text and more', [['t', 'h'], ['e', 'i'], ['x', 'g'], ['T', 'H']]) == 'High and mori'

def test_dlfl ():
    assert enc.dec_lfl('High', [['t', 'h'], ['e', 'i'], ['x', 'g'], ['T', 'H']]) == 'Text'

class TestPorta:
    def test_enc (self):
        cipher = enc.Porta()

        assert cipher.encrypt('DEFEND THE EAST WALL 1', 'War') == 'SRXTAV GZT WPFB JSNY 1'
        assert cipher.encrypt('DEFEND THE EAST WALL', 'War') == 'SRXTAV GZT WPFB JSNY'

        ccipher = enc.Porta(alphabet= {
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
            })

        assert ccipher.encrypt('DEFEND THE EAST WALL 1', 'War') == 'SRXTAV GZT WPFB JSNY 1'
    
    def test_dec (self):
        cipher = enc.Porta()

        assert cipher.decrypt('SRXTAV GZT WPFB JSNY 1', 'War') == 'DEFEND THE EAST WALL 1'
        assert cipher.decrypt('SRXTAV GZT WPFB JSNY', 'War') == 'DEFEND THE EAST WALL'