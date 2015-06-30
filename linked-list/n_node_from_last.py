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


