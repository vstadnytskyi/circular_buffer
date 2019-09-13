from circular_buffer import CircularBuffer
from circular_buffer_client import CircularBufferClient
from queue import Queue
CircularBufferClient.reset = CircularBufferClient.clear
CBServer = Server = CircularBuffer
CBClient = CircularBufferClient
CBQueue = Queue
