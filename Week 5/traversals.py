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
#   Defines simple traversals for treenode (primitive) trees.
#
#   A primitive tree is is like a node-chain; treenodes linked together
#   We will build different kinds of Trees using primitive trees,
#   just as we built Stacks, QUeues and LLists out of node-chains
#
# These traversals print the data values stored in a primitive tree.

import treenode as tn
import Queue as Q

def in_order(tnode):
    """
    Display the nodes of a tree in pre-order.
    :param tnode: a primitive tree
    :return: nothing
    """
    if tnode is None:
        return
    else:
        in_order(tnode.left)
        print(tnode.data, end=" ")
        in_order(tnode.right)


def pre_order(tnode):
    """
    Display the nodes of a tree in pre-order.
    :param tnode: a primitive tree
    :return: nothing
    """
    if tnode is None:
        return
    else:
        print(tnode.data, end=" ")
        pre_order(tnode.left)
        pre_order(tnode.right)


def post_order(tnode):
    """
    Display the nodes of a tree in pre-order.
    :param tnode: a primitive tree
    :return: nothing
    """
    if tnode is None:
        return
    else:
        post_order(tnode.left)
        post_order(tnode.right)
        print(tnode.data, end=" ")


def breadth_order(tnode):
    """
    Display the nodes of a tree in breadth-order.
    :param tnode: a primitive tree
    :return: nothing
    """
    explore = Q.Queue()
    Queue.enqueue(explore, tnode)

    while explore.size() > 0:
      current = explore.dequeue()
      print(current.get_data(), end=" ")
      left = current.get_left()
      if left is not None:
          explore.enqueue(left)
      right = current.get_right()
      if right is not None:
          explore.enqueue(right)


if __name__ == '__main__':
    # Create the tree we've been using in class
    root = tn.treenode(2)
    a = tn.treenode(7)
    b = tn.treenode(5)
    root.left = a
    root.right = b
    c =  tn.treenode(11)
    d =  tn.treenode(6)
    a.left = c
    a.right = d

    print("Pre-order traversal:", end=" ")
    pre_order(root)
    print()
    print("In-order traversal:", end=" ")
    in_order(root)
    print()
    print("Post-order traversal:", end=" ")
    post_order(root)
    print()
    print("Breadth-order traversal:", end=" ")
    breadth_first_order(root)
    print()
