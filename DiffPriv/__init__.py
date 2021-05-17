
"""
DiffPriv is a package focused on privacy, with differential privacy and encryption schemes.

.. include:: ../README.md
"""
__docformat__ = "restructuredtext"

# Sanity Check Imports
import warnings
import json
from urllib import request

# Dependecy Imports
import sys
import csv
import webbrowser
import math
import random
import numpy

# Local
from . import diff
from . import enc
from . import cli

# Metadata
__version__ = 'v1.0.0-beta'
"""Package Version"""
__stable__ = True
"""If package is stable or not."""
__source__ = 'https://github.com/Quantalabs/DiffPriv'
"""Source Repo"""
__docs__ = 'https://diffpriv.readthedocs.io'
"""Documentation URL"""

def _sanity_check():
    # Import Requirements
    try:
        import numpy as np
    except ImportError: # pragma: no cover
        raise ImportError(' \
            Please make sure you have numpy installed. If you have cloned the package from the source, then use: \
                pip install -r requirements.txt \
        ')
    
    url = f'https://pypi.python.org/pypi/DiffPriv/json'
    releases = json.loads(request.urlopen(url).read())['releases']
    latest_version = list(releases.items())[-1]

    try:
        assert __version__ == latest_version[0] # skipcq: BAN-B101
    except AssertionError:  # pragma: no cover
        # We ignore code coverage for this because there is no way to test this through pytest, but it has been tested manually
        warnings.warn(
            '\u001b[33m \n'
            'You have DiffPriv '+__version__+', however, newer versions are avaliable. Use \n'
            '   pip install --upgrade DiffPriv \n'
            'to upgrade your package. \u001b[0m'    
        )

_sanity_check()

del _sanity_check
