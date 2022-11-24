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
#   Defines simple functions for treenode (primitive) trees.
#

import treenode as tn

def isLeaf(tnode):
    """
    Purpose:
        Determine a tree is a leaf node.
    Pre-conditions:
        :param tnode: a treenode
    Post-conditions:
        none
    Return
        :return: True is the treenode has no children
    """
    return tnode is not None \
       and tnode.left is None \
       and tnode.right is None


def height(tnode):
    """
    Purpose:
        Determine the height of a tree.
        The height is defined as the length of the longest path
        from the root to any leaf.
    Pre-conditions:
        :param tnode: a treenode
    Post-conditions:
        none
    Return
        :return: the height of the tree as an integer
    """
    if tnode is None:
        return 0
    else:
        lh = height(tnode.left)
        rh = height(tnode.right)
        return 1 + max(lh, rh)


def member(tnode, val):
    """
    Purpose:
        Determine if val is stored as data in a tree.
    Pre-conditions:
        :param tnode: a treenode
    Post-conditions:
        none
    Return
        :return: the height of the tree as an integer
    """
    if tnode == None:
        return False
    elif tnode.data == val:
        return True
    else:
        return member(tnode.left, val) \
            or member(tnode.right, val)


def count(tnode):
    """
    Purpose:
        Determine the number of nodes in the tree.
    Pre-conditions:
        :param tnode: a treenode
    Post-conditions:
        none
    Return
        :return: the number of nodes as an integer
    """
    if tnode == None:
        return 0
    else:
        return 1 + count(tnode.left) \
                 + count(tnode.right)



if __name__=='__main__':
    # Create the tree we've been using in class
    atree = tn.treenode(2)
    a = tn.treenode(7)
    b = tn.treenode(5)
    atree.left = a
    atree.right = b
    c = tn.treenode(11)
    d = tn.treenode(6)
    a.left = c
    a.right = d
    # test height
    test_suite1 = [
                    {"inputs": [None],
                     "outputs": 0,
                     "reason": "empty tree"},
                    {"inputs": [tn.treenode(5)],
                     "outputs": 1,
                     "reason": "tree with one node"},
                    {"inputs": [atree],
                     "outputs": 3,
                     "reason": "small example from class"}
                 ]
    for test in test_suite1:
        inputs = test['inputs']
        expected = test['outputs']
        actual = height(inputs[0])
        if actual != expected:
            print('Error: height returned', actual, '(expected:', expected, ' --', test['reason'], ')')

    # test member
    test_suite2 = [
                    {"inputs": [None, 1],
                     "outputs": False,
                     "reason": "empty tree"},
                    {"inputs": [tn.treenode(5), 1],
                     "outputs": False,
                     "reason": "tree with one node, value not in tree"},
                    {"inputs": [tn.treenode(5), 5],
                     "outputs": True,
                     "reason": "tree with one node, value in tree"},
                    {"inputs": [atree, 2],
                     "outputs": True,
                     "reason": "small example from class, value in root"},
                    {"inputs": [atree, 11],
                     "outputs": True,
                     "reason": "small example from class, value in leaf"},
                    {"inputs": [atree, 7],
                     "outputs": True,
                     "reason": "small example from class, value in tree"},
                    {"inputs": [atree, 200],
                     "outputs": False,
                     "reason": "small example from class, value not in tree"}
                 ]
    for test in test_suite2:
        inputs = test['inputs']
        expected = test['outputs']
        actual = member(inputs[0], inputs[1])
        if actual != expected:
            print('Error: member returned', actual, '(expected:', expected, ' --', test['reason'], ')')

    # test count
    test_suite3 = [
                    {"inputs": [None],
                     "outputs": 0,
                     "reason": "empty tree"},
                    {"inputs": [tn.treenode(5)],
                     "outputs": 1,
                     "reason": "tree with one node"},
                    {"inputs": [atree],
                     "outputs": 5,
                     "reason": "small example from class"}
                 ]
    for test in test_suite3:
        inputs = test['inputs']
        expected = test['outputs']
        actual = count(inputs[0])
        if actual != expected:
            print('Error: count returned', actual, '(expected:', expected, ' --', test['reason'], ')')

    print("testing complete")

