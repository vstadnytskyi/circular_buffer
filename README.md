
# Overview
This module provides few simple classes with intuitive approach to store data in a buffer. This module is pure Python package. The module has two different data structures implemented using numpy array: the first one is circular buffer and next one is queue. Both structures have common attribute with numpy arrays, such as shape, size and dtype.

# Circular Buffer
Circular Buffer implemented using numpy array of fixed shape (variable upon initialization). The last known entry in the circular buffer is tracked via a pointer. This module has several simple and convenient functions allowing seamless retrieval of data.

# Queue
Queue implemented using numpy array of fixed shape (variable upon initialization). This buffer has two main attributes, rear which return the index of the rear of the Queue and length which returns how many unread points are available. To add data the function enqueue is used which increment both the rear pointer and the length. To read the data the dequeue function is used. Internally, the rear pointer is used to keep track where is the end of the queue. The length can be used to peek inside and see how many elements are available to read. This data structure is convenient for buffering data that comes from a data acquisition unit. The data can be later retrieved for further analysis by FIXIT
