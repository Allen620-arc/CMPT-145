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
#   The Maximum Path Problem
# Given a Binary Tree (not necessarily a Binary Search Tree)
# containing (positive and negative) numbers,
# Find the path from root to leaf that has the maximum sum


import random as rand
import time


# a quick and dirty implementation of TreeNodes
class Treenode(object):
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def is_leaf(self):
        return self.left is None and self.right is None


def random_tree(h, lor=-200, hir=200):
    """
    Construct a complete binary tree of height h with
    randomly chosen data values
    :param h: the height of the tree
    :param lor: an integer
    :param hir: an integer, lor <= hir
    :return: a complete binary TreeNode of height h
    """
    if h == 1:
        return Treenode(rand.randint(lor, hir))
    else:
        return Treenode(rand.randint(lor, hir),
                        random_tree(h - 1, lor, hir),
                        random_tree(h - 1, lor, hir))


# Brute force solution: check all possible paths
def max_path(atree):
    """
    Find the maximum sum of all paths from root to leaf
    in atree.
    :param atree: A TreeNode
    :return: the maximum sum
    """
    if atree is None:
        return 0
    else:
        left = max_path(atree.left)
        right = max_path(atree.right)
        return max(left, right) + atree.data


# Greedy solution
# Note: this algorithm may not return the true maximum!
def greedy_path(atree):
    """
    Find the maximum sum of all paths from root to leaf
    in atree.
    :param atree: A TreeNode
    :return: the maximum sum
    """
    if atree.is_leaf():
        return atree.data
    elif atree.left.data > atree.right.data:
        # the left branch seems promising
        return atree.data + greedy_path(atree.left)
    else:
        # the right branch seems promising
        return atree.data + greedy_path(atree.right)


if __name__ == '__main__':
    # build the tree; O(2^N) time!
    height = 21
    maxval = 100
    print('Building tree...')
    start = time.process_time()
    some_tree = random_tree(height)
    end = time.process_time()
    print('...took:', end - start, 'seconds')

    print('Brute Force Implementation:')
    start = time.process_time()
    result = max_path(some_tree)
    end = time.process_time()
    print("Result:", result, 'Time:', end - start)

    print('Greedy Implementation:')
    start = time.process_time()
    result = greedy_path(some_tree)
    end = time.process_time()
    print("Result:", result, 'Time:', end - start)
