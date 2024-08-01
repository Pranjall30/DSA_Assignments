class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_index(self, index, data):
        new_node = Node(data)
        if index == 0:
            new_node.next = self.head
            self.head = new_node
            return
        current = self.head
        for _ in range(index - 1):
            if current is None:
                return
            current = current.next
        new_node.next = current.next
        current.next = new_node

    def delete_at_index(self, index):
        if index == 0:
            if self.head is None:
                return
            self.head = self.head.next
            return
        current = self.head
        for _ in range(index - 1):
            if current is None or current.next is None:
                return
            current = current.next
        if current.next is None:
            return
        current.next = current.next.next

    def size(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count

    def is_empty(self):
        return self.head is None

    def append(self, data):
        if self.head is None:
            self.head = Node(data)
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = Node(data)

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def merge(self, other):
        if self.head is None:
            self.head = other.head
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = other.head

    def interleave(self, other):
        if self.head is None:
            self.head = other.head
        else:
            current_self = self.head
            current_other = other.head
            while current_self and current_other:
                next_self = current_self.next
                next_other = current_other.next
                current_self.next = current_other
                current_other.next = next_self
                current_self = next_self
                current_other = next_other

    def get_middle(self):
        if self.head is None:
            return None
        slow = fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow.data

    def index_of(self, value):
        index = 0
        current = self.head
        while current:
            if current.data == value:
                return index
            current = current.next
            index += 1
        return -1

    def split_at_index(self, index):
        if index == 0:
            return
        current = self.head
        for _ in range(index - 1):
            if current is None or current.next is None:
                return
            current = current.next
        if current.next is None:
            return
        second_head = current.next
        current.next = None
        second_list = LinkedList()
        second_list.head = second_head
        return second_list

    def rotate_right(self, k):
        if self.head is None or k == 0:
            return
        length = self.size()
        k = k % length
        if k == 0:
            return
        slow = fast = self.head
        for _ in range(k):
            fast = fast.next
        while fast.next:
            slow = slow.next
            fast = fast.next
        fast.next = self.head
        self.head = slow.next
        slow.next = None

    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        print()

# Printing the linked list
ll = LinkedList()
for i in range(1, 7):
    ll.append(i)
ll.display()  

# 1. Insert at specifc index
ll.insert_at_index(1, 5)
ll.display()  

# 2. Delete at specific index
ll.delete_at_index(1)
ll.display()  

# 3. Size of linked list
print(ll.size())  

# 4. Linked List is empty or not
print(ll.is_empty())  

# 5. Rotate linked list by right
ll.rotate_right(2)
ll.display()  

# 6. Reversing linked list
ll.reverse()
ll.display()  

# 8. Prepends element
ll.prepend(0)
ll.display()  # Output: 0 1 3 5

# 9. Merging two linked lists
ll2 = LinkedList()
for i in range(5, 8):
    ll2.append(i)
ll.merge(ll2)
ll.display()  

# 10. Interleaves two linked lists
ll3 = LinkedList()
for i in range(7, 11):
    ll3.append(i)
ll.interleave(ll3)
ll.display()  

# 11. Returns the middle element
print(ll.get_middle())  

# 12. Index of 1st occurence of element
print(ll.index_of(2))  

# 13. Split the two linked list at specified index
ll4 = ll.split_at_index(5)
ll.display()  

ll4.display()  