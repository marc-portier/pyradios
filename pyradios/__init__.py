import logging
from logging import NullHandler
from pyradios.radios import RadioBrowser
from pyradios.facets import RadioFacets

# warning: setup.py assumes strict single quotes on the line below
__version__ = '0.0.22'

__all__ = ["RadioBrowser", "RadioFacets"]

logging.getLogger(__name__).addHandler(NullHandler())
