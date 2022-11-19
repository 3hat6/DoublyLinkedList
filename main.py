from Boom import DoublyLinkedList


def mult10(x):
    return x // 25


def div(x):
    return True if x % 2 == 0 else False


l1 = DoublyLinkedList()
l2 = DoublyLinkedList()

# l1.push_front(777)
# l1.push_back(666)
# l1.insert(1, 2, 3, 4, "|")
# l1.display()
# l1.begin()
# l1.end()
# print(l1.empty())
# print(l1.size())
# l1.clear()
# print('after cleaning')
# l1.display()
l1.insert(50, 4, 6)
l2.insert(1, 3, 5)
l1.emplace(50, mult10)
l1.splice(l2)
# l1.display()
l1.remove_if(func=div)
l1.display()
l1.insert(100, 100, 52, 55, 99, 99, 99, 500, 500, 155, 155)
l1.unique()
l1.display()