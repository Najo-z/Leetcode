#!/usr/bin/env python3

class Node:
    def __init__(self, val : int = 0) -> None:
        self.val = val
        self.next = None
    
def list_add(node : Node, val : int):
    while node.next != None:
        node = node.next
    n = Node(val)
    node.next = n

def list_print(node : Node):
    while node != None:
        

start = Node(1)