  
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