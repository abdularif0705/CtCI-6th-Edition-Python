from chapter_02.linked_list import LinkedList


def intersection(list1, list2):
    if list1.head is None or list2.head is None:
        return False
    if list1.tail != list2.tail:
        return False

    shorter = list1 if len(list1) < len(list2) else list2
    longer = list1 if len(list1) > len(list2) else list2

    diff = len(longer) - len(shorter)

    for _ in range(diff):
        longer.head = longer.head.next

    while longer.head != shorter.head:
        shorter.head = shorter.head.next
        longer.head = longer.head.next

    # return any one
    return longer.head


def test_linked_list_intersection():
    list1 = LinkedList([-1, 0, 1, 2, 3, 4, 5, 6])
    list2 = LinkedList([10, 11, 12, 13])

    # 3rd node from list2 is replaced and attaches to the 5th node in list1
    # In jaav it's list2.next.next = list1.next.next.next.next;
    list2.head.next.next = list1.head.next.next.next.next
    list2.tail = list2.head.next.next.next.next.next

    print(list1)
    print(list2)

    print('the head node of the intersecting list is:',intersection(list1, list2))


test_linked_list_intersection()
