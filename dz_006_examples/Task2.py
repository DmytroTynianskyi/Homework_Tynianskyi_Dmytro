# Завдання 2

# Взявши за основу код прикладу example_5.py, розширте функціональність класу MyList,
# додавши методи очищення списку, додавання елемента у довільне місце списку, видалення елемента з кінця та довільного місця списку.

class MyList(object):
    """Класс списка"""

    # Внутренний класс элемента списка
    class _ListNode(object):
        __slots__ = ('value', 'prev', 'next')

        def __init__(self, value, prev=None, next=None):
            self.value = value
            self.prev = prev
            self.next = next

        def __repr__(self):
            return 'MyList._ListNode({}, {}, {})'.format(self.value, id(self.prev), id(self.next))

    # Внутренний класс итератора
    class _Iterator(object):
        def __init__(self, list_instance):
            self._list_instance = list_instance
            self._next_node = list_instance._head

        def __iter__(self):
            return self

        def __next__(self):
            if self._next_node is None:
                raise StopIteration

            value = self._next_node.value
            self._next_node = self._next_node.next

            return value

    def __init__(self, iterable=None):
        self._length = 0
        self._head = None
        self._tail = None

        if iterable is not None:
            for element in iterable:
                self.append(element)

    def append(self, element):
        node = MyList._ListNode(element)

        if self._tail is None:
            self._head = self._tail = node
        else:
            self._tail.next = node
            node.prev = self._tail
            self._tail = node

        self._length += 1

    def __len__(self):
        return self._length

    def __repr__(self):
        return 'MyList([{}])'.format(', '.join(map(repr, self)))

    def __getitem__(self, index):
        if not 0 <= index < len(self):
            raise IndexError('list index out of range')

        node = self._head
        for _ in range(index):
            node = node.next

        return node.value

    def __iter__(self):
        return MyList._Iterator(self)

    def clear(self):
        """Очищення списку"""
        self._head = None
        self._tail = None
        self._length = 0

    def insert(self, index, element):
        """Вставка елемента у довільне місце списку"""
        if not 0 <= index <= self._length:
            raise IndexError('list index out of range')

        new_node = MyList._ListNode(element)

        if index == 0:
            # Вставка на початок
            new_node.next = self._head
            if self._head:
                self._head.prev = new_node
            self._head = new_node
            if self._tail is None:
                self._tail = new_node
        elif index == self._length:
            # Вставка в кінець
            self.append(element)
            return
        else:
            # Вставка у середину
            current_node = self._head
            for _ in range(index - 1):
                current_node = current_node.next
            new_node.next = current_node.next
            new_node.prev = current_node
            current_node.next.prev = new_node
            current_node.next = new_node

        self._length += 1

    def pop(self):
        """Видалення елемента з кінця списку"""
        if self._tail is None:
            raise IndexError('pop from empty list')

        value = self._tail.value
        self._tail = self._tail.prev

        if self._tail is None:
            self._head = None
        else:
            self._tail.next = None

        self._length -= 1
        return value

    def remove_at(self, index):
        """Видалення елемента з довільного місця списку"""
        if not 0 <= index < self._length:
            raise IndexError('list index out of range')

        if index == 0:
            # Видалення першого елемента
            value = self._head.value
            self._head = self._head.next
            if self._head:
                self._head.prev = None
            else:
                self._tail = None
        elif index == self._length - 1:
            # Видалення останнього елемента
            return self.pop()
        else:
            # Видалення елемента з середини
            current_node = self._head
            for _ in range(index):
                current_node = current_node.next

            value = current_node.value
            current_node.prev.next = current_node.next
            current_node.next.prev = current_node.prev

        self._length -= 1
        return value


def main():
    # Створення списку
    my_list = MyList([1, 2, 3, 4, 5])

    # Тестування нових методів
    print("Initial list:", my_list)

    my_list.insert(2, 9)
    # MyList([1, 2, 9, 3, 4, 5])
    print("After inserting 9 at index 2:", my_list)

    my_list.remove_at(2)
    print("After removing at index 2:", my_list)  # MyList([1, 2, 3, 4, 5])

    my_list.pop()
    print("After popping the last element:", my_list)  # MyList([1, 2, 3, 4])

    my_list.clear()
    print("After clearing the list:", my_list)  # MyList([])


if __name__ == '__main__':
    main()
