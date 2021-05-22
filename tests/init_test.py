  
import os
import sys
import json
from urllib import request

currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

# This will test the sanity check function which is run on import.
import DiffPriv

def test_metadata():
    url = f'https://pypi.python.org/pypi/DiffPriv/json'
    releases = json.loads(request.urlopen(url).read())['releases']
    latest_version = list(releases.items())[-1]

    assert DiffPriv.__name__ == 'DiffPriv'
    assert DiffPriv.__version__ == 'v1.0.0-beta'
    assert DiffPriv.__stable__ == True
    assert DiffPriv.__source__ == 'https://github.com/Quantalabs/DiffPriv'
    assert DiffPriv.__docs__ == 'https://diffpriv.readthedocs.io'