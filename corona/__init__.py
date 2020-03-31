VERSION = "0.0.1"
__version__ = VERSION
__license__ = "MIT"
__author__ = "NANI"

from .client import Client
from .objects import *
from .router import Router
from .http import APIError, NotFound
