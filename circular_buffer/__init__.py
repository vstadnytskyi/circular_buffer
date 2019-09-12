
from ._version import get_versions
__version__ = get_versions()['version']
del get_versions

from .circular_buffer import CircularBuffer
from .queue import Queue
