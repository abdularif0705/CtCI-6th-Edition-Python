from linked_list import LinkedList

# Memory O(n), Time O(n)
def remove_dups(ll):
    current = ll.head
    previous = None # null
    hash_set = set()

    while current:
        if current.value in hash_set:
            previous.next = current.next # skip duplicate value
        else:
            hash_set.add(current.value) # add to hash table/map/set
            previous = current # increment previous
        current = current.next # increment current
    # ll.tail = previous
    # print(ll,'\n')

    # ll = previous
    # print(ll,'\n')

    # return ll

# Memory O(1), Time O(n^2)
def remove_dups_followup(ll):
    runner = current = ll.head

    while current:
        runner = current
        while runner.next:
            if runner.next.value == current.value:
                runner.next = runner.next.next
            else:
                runner = runner.next # move to the next node of the runner linked list
        current = current.next


def main():
    ll = LinkedList.generate(100, 0, 9)
    print("Original Linked List: \n", ll, "\n==============================\n")
    remove_dups(ll)
    print("New Linked List: \n", ll, "\n==============================\n")

    ll = LinkedList.generate(100, 0, 9)
    print("Original Linked List: \n", ll, "\n==============================\n")
    remove_dups_followup(ll)
    print("New Linked List: \n", ll, "\n==============================\n")

main()