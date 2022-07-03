'''
2.1 Write code to remove duplicates from an unsorted linked list
'''

'''
Questions:

1) Do the numbers have a range? If the range is small enough, we can use a bit vector
to check for duplicates. Also indicates if we can use negative numbers as flags

2) Is it a singly linked list or a doubly linked list?

3) Can we rearrange the list nodes or do they have to be in the same order?

4) does it matter which duplicate is removed? should the earliest be left in?
'''

'''
Approach: I'm going to assume its a singly linked list and there are no bounds on numbers.
I'm going to assume the earliest instance of the numbers should remain in the list. and I will
assume order of the list should not change.

I'm going to maintain a set of seen numbers. I'll also
maintain a prev pointer and a curr pointer. if curr is looking at a value thats in the set
of previously seen value, I'll remove the node with the help of prev.
'''
from unicodedata import east_asian_width


class Node:
    def __init__(self, val, next) -> None:
        self.val = val
        self.next = next

def removeDuplicatesFromUnsortedList(head: Node):
    s = set()
    sentinel = Node(-1, head)
    prev = sentinel
    curr = head
    while curr is not None:
        if curr.val not in s:
            s.add(curr.val)
            prev = curr
            curr = curr.next
        else:
            nxt = curr.next
            curr.next = None
            curr = nxt
            prev.next = curr
    return sentinel.next

'''
2.1 Follow Up - How would you solve this if a temporary buffer is not allowed?

Approach: O(n^2). For each linked list node, I'm going to shift it forward until i find a node
with the same value. When I do, I'll delete that duplicate node. I'll keep doing this until the end of the list.
In the end, I'll reverse the list to maintain the initial order.

Better approach. Still O(n^2). Maintain 2 pointers. First pointer looks at a given node. Second pointer looks
ahead of first and checks if any nodes match the value of the first pointer's node. if so, delete that node. 
'''

def followUp(head: Node):
    first = head
    while first is not None:
        second = first.next
        prev = first
        while second is not None:
            if second.val == first.val:
                nxt = second.next
                second.next = None
                second = nxt
                prev.next = second
            else:
                prev = second
                second = second.next
        first = first.next
    return head

# Go back and do the additional questions for arrays chapter. You missed them. 