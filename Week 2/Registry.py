# CMPT 145 Course material
# Copyright (c) 2017-2020 Michael C Horsch
# All rights reserved.
#
# This document contains resources for homework assigned to students of
# CMPT 145 and shall not be distributed without permission.  Posting this 
# file to a public or private website, or providing this file to a person 
# not registered in CMPT 145, constitutes Academic Misconduct, according 
# to the University of Saskatchewan Policy on Academic Misconduct.

# Synopsis:
#   Defines the Registry ADT
#   A registry records a Boolean value for a range of integers.
#   It can be used to record observations or events.

class Registry(object):

    def __init__(self, size, value):
        """
        Purpose:
            Initialize a registry of a give size filled with the 
            given value
        Pre-conditions:
            size: number of elements in the registry
            value: the default initial value for all elements
        """
        self.__reg = [value for i in range(size)]


    def set(self, i):
        """
        Purpose:
            Set the registry element at i to True
        Pre-conditions:
            i: an index, in the correct range for reg
        Post-conditions:
            the registry value at i is set to True
        Return:
            (none)
        """
        self.__reg[i] = True


    def reset(self, i):
        """
        Purpose:
            Set the registry element at i to False
        Pre-conditions:
            i: an index, in the correct range for reg
        Post-conditions:
            the registry value at i is set to False
        Return:
            (none)
        """
        self.__reg[i] = False


    def is_registered(self, i):
        """
        Purpose:
            Returns the value stored at registry element i
        Pre-conditions:
            i: an index, in the correct range for reg
        Post-conditions:
            (none)
        Return:
            the value stored at element i
        """
        return self.__reg[i]
