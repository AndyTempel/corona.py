VERSION = "0.0.2"
__version__ = VERSION
__license__ = "MIT"
__author__ = "NANI"

from .client import Client
from .http import APIError, NotFound
from .objects import *
from .router import Router
