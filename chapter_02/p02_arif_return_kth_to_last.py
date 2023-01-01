from linked_list import LinkedList
import random

# O(n) runtime
def kth_to_last(ll, k):
    leader = follower = ll.head # this starts them on the first node of the Linked List
    count = 0
    print('head of Linked List is',ll.head,'\n')

    ll = ll.head # set to first node so it can increment thru the whole Linked List
    while ll: # while ll has a value on it's current node, we could swap this with 'leader' instead as well
        if count >= k:
            follower = follower.next
        count+=1
        ll = ll.next

    return follower

def main():
    ll = LinkedList.generate(100, 0, 999)
    print("Linked List: \n", ll, "\n==============================\n")

    k = random.randint(1, 5)
    print("k =",k,'\n',k,'th to last element is', kth_to_last(ll, k))

main()