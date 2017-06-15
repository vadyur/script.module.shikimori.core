import os, sys

cur = os.path.dirname(__file__)
path = os.path.join(cur, '../../resources/lib')
sys.path.insert(0, os.path.normpath(path))
import pyshiki

from pyshiki import Api
from wrappers import *

