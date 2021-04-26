# Import Requirements
try:
    import numpy as np
except ImportError: # pragma: no cover
    raise ImportError(' \
        Please make sure you have numpy installed. If you have cloned the package from the source, then use: \
            pip install -r requirements.txt \
    ')
try:
    import luddite
except ImportError: # pragma: no cover
    raise ImportError(' \
        Please make sure you have luddite installed. If you have cloned the package from the source, then use: \
            pip install -r requirements.txt \
    ')

import warnings
import sys

# Local
from . import diff
from . import enc
from . import cli

# Metadata
__version__ = '0.1.1'
__stable__ = True
__source__ = 'https://github.com/Quantalabs/DiffPriv'
__docs__ = 'https://diffpriv.readthedocs.io'

def _sanity_check():
    # Check for any new versions of the package
    try:
        assert __version__ == luddite.get_version_pypi("DiffPriv")
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