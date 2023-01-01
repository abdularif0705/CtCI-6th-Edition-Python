from linked_list import LinkedList


def is_palindrome(ll):
    fast = slow = ll.head  # two runners to go through array
    stack = []  # initialize an array (which has pop() built into it in Python)

    # while fast is not None and fast.next is not None:
    while fast and fast.next:
        stack.append(slow.value)
        slow = slow.next
        fast = fast.next.next

    # if fast has a value left in it that means the linked list has an odd number and slow is currently in the middle
    # node, so we move it over by 1 to start on the 2nd half of the list
    if fast:
        slow = slow.next

    # checking if 1st and 2nd half of list mirror each other
    while slow:
        if slow.value != stack.pop():
            return False
        slow = slow.next

    return True


ll_true = LinkedList([1, 2, 3, 4, 5, 4, 3, 2, 1])
print('linked_list:', ll_true, "is a palindrome:", is_palindrome(ll_true))
ll_false = LinkedList([1, 2, 3, 4, 5, 6, 7, 8, 9])
print('linked_list:', ll_false, "is a palindrome:", is_palindrome(ll_false))
