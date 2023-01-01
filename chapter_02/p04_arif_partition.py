from linked_list import LinkedList

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:

    def partition(ll, x): # x is the partition''' '''

    # def partition(self, head: ListNode, x: int) -> ListNode: # x is the partition
        '''
        Creating two lists and adding value based on whether current node's value
        is < or >= the partition node 
        '''    
        left, right = ListNode(), ListNode() # left and right dummy nodes (empty nodes we create)
        ltail, rtail = left, right # points to last element in left and right tails

        current = ll.tail = ll.head


        while current:
            if current.value < x.value:
                ltail.next = current
                ltail = ltail.next # update tail to point to end of left list
            else:
                rtail.next = current
                rtail = rtail.next
            current = current.next

        # connect left list to right list
        ltail.next = right.next # right is a dummy node so right.next is gonna be the 1st REAL node
        rtail.next = None # We have to terminate our list which means last Node has to point to null

        return left.next # left is a dummy node so left.next is gonna be the 1st node in our list       


    # def example():
        # ll = LinkedList.generate(10, 0, 9)
        # print("Original LinkedList:\n",ll)
        # ll = partition(ll, ll.head)
        # print("After Partition LinkedList:\n",ll)


    if __name__ == "__main__":
        ll = LinkedList()
        ll.add_multiple([3, 5, 8])
        partition_node = ll.add(5) # only have access to the middle node for this question
        ll.add_multiple([10, 2, 1])

        print("Original LinkedList:\n",ll)
        partition(ll, partition_node)
        print("After Partition LinkedList:\n",ll)

        # example()


