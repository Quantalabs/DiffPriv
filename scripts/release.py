"""
Updates release numbers across the project when release is published on github.
"""

import DiffPriv

version = [char for char in DiffPriv.__version__]
del version[0]
del version[0]
del version[0]
del version[0]
del version[0]
new_version = int("".join(version))+1
version = [char for char in DiffPriv.__version__]
version[5] = str(new_version)
version = "".join(version)

with open('setup.cfg', 'r') as cfg:
    cfg_read = cfg.readlines() 
    cfg_read[2] = 'version = '+version+'\n'

with open('setup.cfg', 'w') as cfg:
    cfg.writelines(cfg_read)

with open('setup.py', 'r') as py:
    py_read = py.readlines()
    py_read[7] = '    version="'+version+'",\n'

with open('setup.py', 'w') as py:
    py.writelines(py_read)

with open('DiffPriv/__init__.py', 'r') as init:
    init_read = init.readlines()
    init_read[27] = "__version__ = '"+version+"'\n"

with open('DiffPriv/__init__.py', 'w') as init:
    init.writelines(init_read)