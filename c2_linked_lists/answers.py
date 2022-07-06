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

'''
head = createListWithDuplicates(0, 1, 10)
for i in range(1, 11):
    print(kthElementOfSinglyLinkedList(head, i))
'''

'''
2.3 delete middle node - given only the middle node inside of a singly linked list, delete the middle node
inside the list. you are not given the list, and you don't need to return anything. 

if you were given the list, then it would be easy. just iterate through the list until the next node is 
the middle node, then delete that node. but in this case you are not given the list.

Approach: swap the numbers of the middle node with every node after it, essentially "pushing" the number down the list.
You have to do this with the number instead of the node, because if you do it with the node, you will cut the list in half. 
Maintain a prev pointer as well. Once you reach the end of the list, last node will contain the middle node's value, and prev
will be pointing to the second to last value. Use prev to snip the last node off. 
'''

def deleteMiddleNode(middle: Node):
    if middle is None:
        return
    curr = middle
    prev = None
    while curr.next is not None:
        temp = curr.next.val
        curr.next.val = curr.val
        curr.val = temp
        prev = curr
        curr = curr.next
    if prev is None:
        # this doesn't work, but not sure how else to delete the node the pointer is pointing to in python. 
        del middle
    else:
        prev.next = None

# helper method that returns the middle node from a linked list. used for testing.
def getMiddleFromList(head) -> Node:
    if head is None:
        return head
    curr = head
    fast = head.next
    while fast is not None and fast.next is not None:
        curr = curr.next
        fast = fast.next
        if fast is not None:
            fast = fast.next
    return curr

''' 
head = createListWithDuplicates(0, 3, 4)
printList(head)
middle = getMiddleFromList(head)
deleteMiddleNode(middle)
printList(head)
'''

'''
2.4 Partition around X. Write code to partition a singly linked list around a value X, such that all nodes with values < X come before all nodes
with values >= X

Brute force: iterate through the list, if a number is < X, save it to one map, if its >= X, save it to a different map. Then construct a new list using that
information

Optimized Approach: Iterate through the list to find the tail (last node in the list). Then, iterate again. If an element < X, move forward. If it's >= X, append it
to end of the list, delete it from its current position, then move forward. When you reach the tail node, exit. Assumption: order doesn't matter so long as all 
elements < X are before all elements >= X. If this assumption is correct, then the tail will be in the correct position no matter what - either its at the end of all numbers,
or its at the beginning of all numbers >= X. It's in the correct position anyway. 
'''

def partitionAroundX(head, partitionVal):
    if head is None:
        return head
    curr = head
    while curr.next is not None:
        curr = curr.next
    tail = curr
    
    sentinel = Node(-1)
    sentinel.next = head
    curr = head
    prev = sentinel
    higherCurr = tail
    while curr != tail:
        if curr.val >= partitionVal:
            next = curr.next
            prev.next = next
            curr.next = None
            higherCurr.next = curr
            higherCurr = higherCurr.next
            curr = next
        else:
            prev = curr
            curr = curr.next
    return sentinel.next

'''
head = createListWithDuplicates(4, 1, 11)
printList(head)
result = partitionAroundX(head, 10)
printList(result)
'''

'''
2.5 Sum Lists - you are given 2 singly linked lists where each node in the list is a digit of a number in reverse order. so 5 -> 1 -> 2 = 215. Sum the 2 lists and return the answer
as a linked list in reverse order. 

Approaches:

1) Form actual ints from the list, sum the ints, then covert the resulting int to a linked list in the desired order
2) Go node by node, keep track of digit and carry.
'''

def sumLists(a, b):
    p1 = a
    p2 = b
    carry = 0
    sentinel = Node(-1)
    curr = sentinel
    while p1 is not None or p2 is not None:
        val1 = val2 = 0
        if p1 is not None:
            val1 = p1.val
            p1 = p1.next
        if p2 is not None:
            val2 = p2.val
            p2 = p2.next
        s = val1 + val2 + carry
        digit = s if s < 10 else s - 10
        carry = 0 if s < 10 else 1
        curr.next = Node(digit, None)
        curr = curr.next
    if carry:
        curr.next = Node(carry)
    return sentinel.next

'''
l1 = Node(7)
l1.next = Node(1)
l1.next.next = Node(6)

l2 = Node(5)
l2.next = Node(9)
l2.next.next = Node(2)

result = sumLists(l1, l2)
printList(result)
'''

'''
2.5 Follow up - Same problem as above, but the digits are in forward order. 

Approaches:
1) Covert the lists to ints, sum the ints, convert the result to a list
2) Go recursively. On each recursive level, call the recursive function on the remainder of the lists. Each level should return the completed list from that point forward, and a carry value. 
You might have to add padding to the beginning of the list if the lists are of uneven size. This is because I assume 1 -> 2 -> 3 -> 4 + 3 -> 4 for example = 1234 + 34, NOT 1234 + 3400.
3) Same as approach 2, but iteratively, using a stack
4) reverse the lists then use the algorithm from initial problem (makes assumption that you can modify input lists)

Approach 1 is the most space efficient, but all 3 have the same time efficiency. You will have to iterate over the lists twice.
'''

def getLengthOfList(l):
    curr = l
    result = 0
    while curr is not None:
        curr = curr.next
        result += 1
    return result

# approach 2
def followup2_5_recursive(a, b):

    def recur(a, b):
        if a is None and b is None:
            return (0, None)
        carry, finishedList = recur(a.next, b.next)
        s = a.val + b.val + carry
        digit = s if s < 10 else s - 10
        carry = 0 if s < 10 else 1
        return (carry, Node(digit, finishedList))

    alength = getLengthOfList(a)
    blength = getLengthOfList(b)
    diff = abs(alength - blength)
    if diff > 0:
        paddingSentinel = Node(-1)
        curr = paddingSentinel
        while diff > 0:
            curr.next = Node(0)
            curr = curr.next
            diff -= 1
        if alength < blength:
            curr.next = a
            a = paddingSentinel.next
        else:
            curr.next = b
            b = paddingSentinel.next

    carry, finishedList = recur(a, b)
    result = finishedList
    if carry:
        result = Node(carry, finishedList)
    return result

# approach 3
def followup2_5_iterative(a, b):
    stack1 = []
    stack2 = []
    curr = a
    while curr is not None:
        stack1.append(curr.val)
        curr = curr.next
    curr = b
    while curr is not None:
        stack2.append(curr.val)
        curr = curr.next
    carry = 0
    sentinel = Node(-1)
    while stack1 or stack2:
        val1 = stack1.pop() if stack1 else 0
        val2 = stack2.pop() if stack2 else 0
        s = val1 + val2 + carry
        digit = s if s < 10 else s - 10
        carry = 0 if s < 10 else 1
        sentinel.next = Node(digit, sentinel.next)
    if carry:
        sentinel.next = Node(carry, sentinel.next)
    return sentinel.next



l1 = Node(2)
l1.next = Node(0)
l1.next.next = Node(0)
l1.next.next.next = Node(0)

l2 = Node(3)
l2.next = Node(2)
l2.next.next = Node(4)

result = followup2_5_recursive(l1, l2)
printList(result)
result = followup2_5_recursive(l1, l2)
printList(result)

l1 = Node(9)
l1.next = Node(9)
l1.next.next = Node(9)

l2 = Node(9)
l2.next = Node(9)
l2.next.next = Node(9)

result = followup2_5_recursive(l1, l2)
printList(result)
result = followup2_5_recursive(l1, l2)
printList(result)
