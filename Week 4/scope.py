# CMPT 145 Course material
# Copyright (c) 2017-2020 Michael C Horsch
# All rights reserved.
#
# This document contains resources for homework assigned to students of
# CMPT 145 and shall not be distributed without permission.  Posting this 
# file to a public or private website, or providing this file to a person 
# not registered in CMPT 145, constitutes Academic Misconduct, according 
# to the University of Saskatchewan Policy on Academic Misconduct.
# 
# Synopsis:
#   Scope Laboratory

# a global variable
duplicates = []

def find_duplicates(alist):
    """
    Purpose:
        Return a list of duplicate values found in alist.
    Pre:
        alist: a list of values
    Post:
        None
    Return:
        A list of duplicates from alist
    """
    uniques = []
    for item in alist:
        if item in uniques:
            duplicates.append(item)
        else:
            uniques.append(item)
    return duplicates



# line = input("Enter some numbers separated by spaces: ")
# numbers = [int(v) for v in line.rstrip().split()]
# print("Duplicates:", find_duplicates(numbers))
# 
# line = input("Enter some numbers separated by spaces: ")
# numbers = [int(v) for v in line.rstrip().split()]
# print("Duplicates:", find_duplicates(numbers))
# 
