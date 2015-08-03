#Write an algorithm to find the kth to last element of a singly linked list. 

def find_n_from_last(head, n):
    current = head
    fast = head
    i = 0
    while i < n:
        fast = fast.next
        i += 1
    while fast != null:
        current = current.next
        fast = fast.next
    print current.data


class Node(object):
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next = next_node
    
    def get_data(self):
        return self.data

    def get_next(self):
        return self.next
    
    def set_next(self, new_next):
        self.next = new_next


