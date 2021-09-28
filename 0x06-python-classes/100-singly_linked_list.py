#!/usr/bin/python3
""" Module singly linked list"""


class Node:
    def __init__(self, data, next_node=None):
        """initialization of node
        Args:
            data (int): Number to store in node
            next_node (Node,  optional): points to next node
        """
        if type(data) is not int:
            raise TypeError("data must be an integer")
        self.__data = data

        if next_node is None or isinstance(next_node, Node):
            self.__next_node = next_node
        else:
            raise TypeError("next_node must be a Node object")

    @property
    def data(self):
        """ Node data getter """
        return self.__data

    @data.setter
    def data(self, value):
        """
        Node data setter
        Args:
            value (int): Value in node
        """
        if type(value) is not int:
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Retrives the next_node value for the current node"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """
        Sets new node
        Args:
            value (Node): value to be inserted in new node
        """
        if value is None or isinstance(value, Node):
            self.__next_node = value
        else:
            raise TypeError("next_npde must be a Node object")


class SinglyLinkedList():
    """Singly-linked list class"""

    def __init__(self):
        """Initializes singly linked list"""
        self.__head = None

    def sorted_insert(self, value):
        """
        Inserts new node - keeping ascending order
        Args:
            value: value of new node
        """
        if type(value) != int:
            raise TypeError("data must be an integer")
        temp = None
        current = self.__head
        new_node = Node(value)
        if current is None:
            new_node.__next_node = None
            self.__head = new_node
        else:
            while current is not None and value > current.data:
                temp = current
                current = current.__next_node
            if temp is None:
                new_node.__next_node = self.__head
                self.__head = new_node
            else:
                temp.__next_node = new_node
                new_node.__next_node = current

    def __str__(self):
        """ operation when print() is called """

        linked_list = []
        current = self.__head
        while current is not None:
            linked_list.append(current.data)
            current = current.__next_node
        return ('\n'.join(str(i) for i in linked_list))
