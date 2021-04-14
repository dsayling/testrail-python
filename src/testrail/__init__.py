import sys

if sys.version_info >= (3, 0):
    from testrail._py3 import *
elif sys.version_info < (3,0):
    from testrail._py2 import *