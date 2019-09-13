#!/bin/env python
# -*- coding: utf-8 -*-
"""Queue
    by Valentyn Stadnytskyi
    created: Nov 4, 2017
    last update: February, 2019

    Queue is an abstract data structure, somewhat similar to Stacks. Unlike stacks, a queue is open at both its ends.
    One end is always used to insert data (enqueue) and the other is used to remove data (dequeue)..


Basic Operations
Queue operations may involve initializing or defining the queue, utilizing it, and then completely erasing it from the memory. Here we shall try to understand the basic operations associated with queues −

enqueue() − add (store) an item to the queue.

dequeue() − remove (access) an item from the queue.

Few more functions are required to make the above-mentioned queue operation efficient. These are −

peek() − Gets the element at the front of the queue without removing it.

isfull() − Checks if the queue is full.

isempty() − Checks if the queue is empty.
"""
__version__  = '1.0.0'

from logging import debug, info, warn, error
from numpy import nan, zeros, ones, asarray, transpose, concatenate
from pdb import pm
import traceback

class Queue(object):
    """
    queue data structure implemented using numpy arrays.

    takes:
        shape = (20,2)
        dtype = 'float64'
    creates numpy array of the give size.
    """
    def __init__(self, shape = (20,2) , dtype = 'float64'):
        """
        the queue has front pointer and the length.
        """
        self.rear = 0 #the end of the quequ, where new date will be enquequ.
        self.length = 0 #length defined as size of the second axis
        if 'float' in dtype:
            self.buffer = zeros(shape, dtype=dtype) * nan
        else:
            self.buffer = zeros(shape, dtype=dtype)


    def enqueue(self,data):
        """
        add (store) an item to the queue.
        """
        from numpy import zeros
        if 'tuple' in str(type(data)) or 'lst' in str(type(data)):
            arr = zeros((len(data),1))
            for idx in range(len(data)):
                arr[idx,0] = data[idx]
        else:
            arr = data
        try:
            for j in range(arr.shape[0]):
                if  self.rear == self.shape[0]-1:
                    self.rear = -1
                self.buffer[self.rear+1] = arr[j]
                self.rear = self.rear + 1
                if self.length == self.shape[0]:
                    pass
                else:
                    self.length += 1
        except Exception:
            error(traceback.format_exc())

    def dequeue(self,N = 0):
        """− remove (access) an item from the queue.
        return N points from the back and move back_pointer
        """
        front = self.rear
        length = self.length
        if length >= N:
            i_pointer = front - length + 1
            debug('i_pointer = %r' %(i_pointer))
            if i_pointer < 0:
                i_pointer = self.shape[1] + (i_pointer)
            j_pointer = front - length + N + 1
            if j_pointer < 0:
                j_pointer = self.shape[1] + (j_pointer)
            debug('front = %r, i = %r , j = %r' %(front,i_pointer,j_pointer))
            data = self.get_i_j(i_pointer,j_pointer)
            self.length -= N
        else:
            data = None
        return data

    ##Few more functions are required to make the above-mentioned queue operation efficient. These are −
    def peek_last(self):
        """Gets the element at the front of the queue without removing it."""
        raise NotImplementedError()

    @property
    def isfull(self):
        """
        Checks if the queue is full.
        """
        return self.length >= self.shape[0]

    @property
    def isempty(self):
        """
        Checks if the queue is empty.
        """
        return self.length == 0

    def reset(self):
        """
        resets the queue by setting front and back equal to 0.
        """
        self.rear = 0 #the last written element
        self.length = 0 #the last read element

    def reshape(self, shape, dtype = None):
        """
        reshapes buffer but also resets it. Takes two parameters as input, shape and dtype.
        dtype atribute can be passed if dtype of the queue needs changes
        """
        from numpy import zeros
        if dtype is None: dtype = self.dtype
        if 'float' in dtype:
            self.buffer = zeros(shape, dtype=dtype) * nan
        else:
            self.buffer = zeros(shape, dtype=dtype)
        self.rear = 0 #the end of the quequ, where new date will be enquequ.
        self.length = 0 #length defined as size of the second axis

    @property
    def size(self):
        """
        returns the size of the circular buffer
        """
        return self.buffer.size

    @property
    def shape(self):
        """
        returns the shape of the circular buffer
        """
        return self.buffer.shape

    @property
    def dtype(self):
        """
        returns the dtype of the circular buffer
        """
        return self.buffer.dtype


####Extra functions that are used for peeking into the queue but not reading the data.
####Important for functioning of the queue
    def get_i_j(self,i,j):
        """
        returns buffer between indices i and j (including index i)
        if j < i, it assumes that buffer wrapped around and will give information
        accordingly.
        NOTE: the user needs to pay attention to the order at which indices
        are passed
        NOTE: index i cannot be -1 otherwise it will return empty array
        """
        if j>i:
            res = self.buffer[i:j]
        else:
            length = self.shape[1] - i +j
            res = self.get_N(N = length, M = j-1)
        return res

    def get_N(self,N,M):
        """
        return N points before index M in the circular buffer
        """
        P = M
        if N-1 <= P:
            result = self.buffer[P+1-N:P+1]
        else:
            result = concatenate((self.buffer[-(N-P-1):], self.buffer[:P+1]),axis = 1)
        return result

    def get_last_N(self,N):
        """
        get into last N
        """
        raise NotImplementedError()

if __name__ == "__main__": # for testing purposes
    from time import time
    import logging
    from tempfile import gettempdir
    logging.basicConfig(#filename=gettempdir()+'/circular_buffer_LL.log',
                        level=logging.DEBUG, format="%(asctime)s %(levelname)s: %(message)s")

    queue = Queue()

    print("Circular buffer library")
    print("two classes: server and client")
    print("server = server() \nclient = client()")
    print("---------------------------")
    print("Server functions")
    print("server.append(data)")
    print("server.get_all()")
    print("server.get_N(N = integer)")
    print("---------------------------")
    print("Client functions")
    print("client.get_all()")
    print("client.get_update()")
    print("client.give_all()")
    print("client.give_N(N = integer)")
    print("---------------------------")
    print("Queue functions")
    print("arr = asarray([[1],[2]])")
    print("queue.enqueue(arr)")
    print("queue.dequeue(N = 1)")
    print("queue.isempty()")
    print("queue.isfull()")
    print("queue.front, queue.back")
    print("queue.size, queue.len, queue.type")
