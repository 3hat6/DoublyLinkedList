class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.start_node = None

    def front(self):
        return self.start_node

    def back(self):
        head_node = self.start_node
        while head_node.next is not None:
            head_node = head_node.next
        return head_node

    def begin(self):
        elem = self.start_node
        while elem is not None:
            print(elem.value, end=' ')
            elem = elem.next

    def end(self):
        elem = self.back()
        while elem is not None:
            print(elem.value, end=' ')
            elem = elem.prev

    def empty(self):
        return True if self.start_node is None else False

    def size(self):
        head_node = self.start_node
        count = 0
        while head_node is not None:
            count += 1
            head_node = head_node.next
        return count

    def clear(self):
        head_node, tail = self.start_node, self.back()
        head_node.next, head_node.value, tail.value, tail.prev = None, None, None, None

    def insert(self, *args):
        if self.start_node is None:
            self.start_node = Node(args[0])
            args = args[1:]
        tail = self.back()
        for elem in args:
            new_elem = Node(elem)
            tail.next, new_elem.prev = new_elem, tail
            tail = new_elem

    def emplace(self, value, func):
        head_node = self.start_node
        tail = head_node
        while tail is not None:
            if tail.value == value:
                tail.value = func(tail.value)
                return tail.value
            tail = tail.next
        return KeyError

    def push_front(self, elem):
        if self.start_node is None:
            head_node = Node(elem)
            self.start_node = head_node
        else:
            new_elem, head_node = Node(elem), self.start_node
            new_elem.next, head_node.prev = head_node, new_elem
            self.start_node, new_elem = new_elem, self.start_node

    def push_back(self, elem):
        if self.start_node is None:
            new_elem = Node(elem)
            self.start_node = new_elem
        else:
            new_elem = Node(elem)
            last_elem = self.back()
            new_elem.prev = last_elem
            last_elem.next = new_elem

    def resize(self, count):
        elem = self.start_node
        while count != 1:
            elem = elem.next
            count -= 1
        elem.next = None

    def splice_array(self, lst):
        last_node = self.back()
        for elem in lst:
            new_node = Node(elem)
            last_node.next, new_node.prev = new_node.value, last_node.value
            last_node = new_node

    def splice(self, lst):
        last_node, first_node = self.back(), lst.start_node
        last_node.next, first_node.prev = first_node, last_node

    def merge(self, lst):
        nodeA, nodeB, node0 = self.start_node, lst.start_node, Node(0)
        tail = node0
        while True:
            if nodeA is None:
                tail.next, nodeB.prev = nodeB.value, tail.value
                break
            elif nodeB is None:
                tail.next, nodeA.prev = nodeA.value, tail.value
                break
            elif nodeA.value >= nodeB.value:
                new_node = Node(nodeB.value)
                tail.next, new_node.prev, nodeB = new_node, tail, nodeB.next
            else:
                new_node = Node(nodeA.value)
                tail.next, new_node.prev, nodeA = new_node, tail, nodeA.next
            tail = tail.next
        return node0.next

    def remove_if(self, func):
        elem = self.start_node
        while elem is not None:
            if func(elem.value):
                if self.back() == elem:
                    print(elem.value)
                    elem.prev.next = None
                elif elem == self.front():
                    elem.next.prev = None
                    self.start_node = elem.next
                else:
                    elem.next.prev, elem.prev.next = elem.prev, elem.next
            elem = elem.next

    def unique(self):
        elem = self.start_node
        while elem.next is not None:
            if elem.value == elem.next.value:
                if self.back() == elem:
                    elem.prev.next = None
                elif elem == self.front():
                    elem.next.prev = None
                    self.start_node = elem.next
                else:
                    elem.next.prev, elem.prev.next = elem.prev, elem.next
            elem = elem.next

    def display(self):
        elem = self.start_node
        while elem is not None:
            print(elem.value, end=' ')
            elem = elem.next
