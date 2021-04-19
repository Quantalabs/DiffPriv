  
import os
import sys
import io

currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

# This will test the sanity check function which is run on import.
import DiffPriv

def test_metadata():
    assert DiffPriv.__name__ == 'DiffPriv'
    assert DiffPriv.__version__ == '0.1.1'
    assert DiffPriv.__stable__ == True
    assert DiffPriv.__source__ == 'https://github.com/Quantalabs/DiffPriv'
    assert DiffPriv.__docs__ == 'https://diffpriv.readthedocs.io'

def test_cli_main():

    old_stdout = sys.stdout # Memorize the default stdout stream
    sys.stdout = buffer = io.StringIO()

    DiffPriv.main()

    sys.stdout = old_stdout # Put the old stream back in place

    whatWasPrinted = buffer.getvalue() # Return a str containing the entire contents of the buffer.
    assert whatWasPrinted == 'DiffPriv \n\
================== \n\
Version - 0.1.1\n\
Stable - True\n\
Source Code - https://github.com/Quantalabs/DiffPriv\n\
Documentation - https://diffpriv.readthedocs.io\n\
\n\
DiffPriv is a python package for differential privacy and other privacy-related tools. Documentation can be accessed via the online documentation or through the built-in python `help()` command.\n'