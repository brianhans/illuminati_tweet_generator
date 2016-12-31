#!python

from __future__ import print_function

class Node(object):

    def __init__(self, data):
        """Initialize this node with the given data"""
        self.data = data
        self.next = None
        self.last = None

    def __repr__(self):
        """Return a string representation of this node"""
        return 'Node({})'.format(repr(self.data))


class LinkedList(object):

    def __init__(self, iterable=None):
        """Initialize this linked list; append the given items, if any"""
        self.head = None
        self.tail = None
        if iterable:
            for item in iterable:
                self.append(item)

    def __iter__(self):
        """
        Best case running time: Om(1) and
        Worst case running time: O(1) because we only return one element and
        don't loop."""
        current = self.head

        while current is not None:
            yield current.data
            current = current.next

    def __repr__(self):
        """Return a string representation of this linked list"""
        return 'LinkedList({})'.format(self.as_list())

    def as_list(self):
        """Return a list of all items in this linked list

        Best case running time: Om(n) and
        Worst case running time: O(n) because we have to loop through all of
        the elements in the linked list to turn it into a list."""

        result = []
        current = self.head
        while current is not None:
            result.append(current.data)
            # result.append(current)
            current = current.next
        return result

    def is_empty(self):
        """Return True if this linked list is empty, or False

        Best case running time: Om(1) and
        Worst case running time: O(1) because we don;t have to iterate
        through any of the elements."""

        return self.head is None

    def length(self):
        """Return the length of this linked list by traversing its nodes
            Best case running time: Om(n) and
            Worst case running time: O(n) because we have to go through all
            the elements to find the count."""

        count = 0
        current = self.head
        while current is not None:
            count += 1
            current = current.next
        return count

    def append(self, item):
        """Insert the given item at the tail of this linked list

        Best case running time: Om(1) and
        Worst case running time: O(1) because we are keeping a reference to
        the head, we don't have to iterate throught any of the elements."""

        new_node = Node(item)
        if self.tail:
            self.tail.next = new_node
        else:
            self.head = new_node
        self.tail = new_node

    def prepend(self, item):
        """Insert the given item at the head of this linked list

        Best case running time: Om(1) and
        Worst case running time: O(1) because we are keeping a reference to
        the head, we don't have to iterate throught any of the elements."""

        new_node = Node(item)
        if self.head:
            new_node.next = self.head
        else:
            self.tail = new_node
        self.head = new_node

    def delete(self, item):
        """Delete the given item from this linked list, or raise ValueError

        Best case running time: Om(1) if item is near the head of the list.
        Worst case running time: O(n) if item is near the tail of the list or
        not present and we need to loop through all n nodes in the list."""
        last_node = None
        current = self.head
        while current is not None:
            if(current.data == item):
                if last_node:
                    last_node.next = current.next
                if self.head == current:
                    self.head = current.next
                if self.tail == current:
                    self.tail = last_node
                current = None
                return
            last_node = current
            current = current.next

        raise ValueError

    def find(self, quality):
        """Return an item from this linked list satisfying the given quality.

        Best case running time: Om(1) if item is near the head of the list.
        Worst case running time: O(n) if item is near the tail of the list or
        not present and we need to loop through all n nodes in the list."""

        current = self.head
        while current is not None:
            if(quality(current.data)):
                return current.data
            current = current.next


class DoublyLinkedList(object):

    def __init__(self, iterable=None):
        """Initialize this linked list; append the given items, if any"""
        self.head = None
        self.tail = None
        if iterable:
            for item in iterable:
                self.append(item)

    def __iter__(self):
        return LinkedListIterator(self)

    def __repr__(self):
        """Return a string representation of this linked list"""
        return 'LinkedList({})'.format(self.as_list())

    def as_list(self):
        """Return a list of all items in this linked list"""
        result = []
        current = self.head
        while current is not None:
            result.append(current.data)
            # result.append(current)
            current = current.next
        return result

    def is_empty(self):
        """Return True if this linked list is empty, or False"""
        return self.head is None

    def length(self):
        """Return the length of this linked list by traversing its nodes"""
        count = 0
        current = self.head
        while current is not None:
            count += 1
            current = current.next
        return count

    def append(self, item):
        """Insert the given item at the tail of this linked list"""
        new_node = Node(item)
        if self.tail:
            self.tail.next = new_node
            new_node.last = self.tail
        else:
            self.head = new_node
        self.tail = new_node

    def prepend(self, item):
        """Insert the given item at the head of this linked list"""
        new_node = Node(item)
        if self.head:
            new_node.next = self.head
            self.head.last = new_node
        else:
            self.tail = new_node
        self.head = new_node



    def delete(self, item):
        """Delete the given item from this linked list, or raise ValueError"""
        last_node = None
        current = self.head
        while current is not None:
            if(current.data == item):
                if last_node:
                    last_node.next = current.next
                    current.next.last = last_node
                if self.head == current:
                    self.head = current.next
                    current.last = None
                if self.tail == current:
                    self.tail = last_node
                current = None
                return
            last_node = current
            current = current.next

        raise ValueError

    def find(self, quality):
        """Return an item from this linked list satisfying the given quality"""
        current = self.head
        while current is not None:
            if(quality(current.data)):
                return current.data
            current = current.next

def test_linked_list():
    ll = LinkedList()
    print(ll)
    ll.append('A')
    print(ll)
    ll.append('B')
    print(ll)
    ll.append('C')
    print(ll)
    print('head: ' + str(ll.head))
    print('tail: ' + str(ll.tail))
    print(ll.length())

    ll.delete('A')
    print(ll)
    ll.delete('C')
    print(ll)
    ll.delete('B')
    print(ll)
    print('head: ' + str(ll.head))
    print('tail: ' + str(ll.tail))
    print(ll.length())

if __name__ == '__main__':
    test_linked_list()
