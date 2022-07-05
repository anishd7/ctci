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

import random


class Node:
    def __init__(self, val, next=None) -> None:
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

def printList(head: Node):
    curr = head
    output = []
    while curr is not None:
        output.append(str(curr.val))
        curr = curr.next
    print(' -> '.join(output))

'''
Helper function for testing to create a randomized list with duplicates

numDuplicates: number of distinct elements you want duplicated. if 0 is passed, will return a list
of all numbers between [minVal, maxVal] where no numbers are duplicated. List is NOT randomized

minVal: smallest number in the list

maxVal: largest number in the list

returns: a list where all numbers between minVal and maxVal are included at least once, and numDuplicates
numbers between [minVal, maxVal] will be duplicated a random number of times and placed randomly in the list.
'''
def createListWithDuplicates(numDuplicates: int, minVal: int, maxVal: int):
    if numDuplicates > maxVal - minVal + 1:
        print("Requesting more distinct duplicate numbers then there are numbers available.")
        return
    deck = []
    for i in range(minVal, maxVal + 1):
        deck.append(i)

    for i in range(numDuplicates):
        j = random.randrange(i, len(deck))
        deck[i], deck[j] = deck[j], deck[i]

    dups = {}
    if numDuplicates > 0:
        for i in range(numDuplicates):
            # arbitrary but random amount of times to duplicate
            dups[deck[i]] = random.randint(1, 5)
    
    i = minVal
    sentinel = Node(-1)
    curr = sentinel
    while i <= maxVal:
        currVal = i
        coin = random.randint(0, 1)
        randomWasChosen = coin and len(dups)
        if randomWasChosen:
            which = random.randrange(0, numDuplicates)
            currVal = deck[which]
            deck[which] -= 1
            if deck[which] == 0:
                del deck[which]
        curr.next = Node(currVal)
        curr = curr.next
        if not randomWasChosen:
            i += 1
    return sentinel.next

'''
head = createListWithDuplicates(3, 1, 10)
printList(head)
# removeDuplicatesFromUnsortedList(head)
followUp(head)
printList(head)
'''

'''
2.2 Write an algorithm to find the kth to last element of a singly linked list

k=1 means last element i suppose

Brute force: iterate through singly linked list, find the length. Then iterate a second time, and once you've 
iterated through length - k elements, return the element you're looking at currently. 

Optimized Approach: Runner's technique. have 2 pointers. 1 pointer is ahead (runner) of the first (slow) by k nodes. 
Once the runner is None (beyond the end of the list), return slow pointer position
'''

def kthElementOfSinglyLinkedList(head: Node, k):
    runner = head
    itr = k
    while itr > 0:
        runner = runner.next
        itr -= 1
    slow = head
    while runner is not None:
        slow = slow.next
        runner = runner.next
    return slow.val

head = createListWithDuplicates(0, 1, 10)
for i in range(1, 11):
    print(kthElementOfSinglyLinkedList(head, i))

'''
2.3 delete middle node - given only the middle node inside of a singly linked list, delete the middle node
inside the list. you are not given the list, and you don't need to return anything. 

if you were given the list, then it would be easy. just iterate through the list until the next node is 
the middle node, then delete that node. but in this case you are not given the list.

Approach: push the middle node until the end of the list. maintain a prev pointer as well. when the middle node
has reached the end of the list, then prev will be pointing to the 2nd to last element, and you can use prev to 
delete the last node.
'''

def deleteMiddleNode(middle: Node):
    pass
    
