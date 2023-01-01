from chapter_02.linked_list import LinkedList


def loop_detection(ll):
    # print(len(ll)) or print(ll) breaks program cuz loop is infinitely long
    fast = slow = ll.head

    print(fast)
    print(slow)

    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
        print(fast)
        print(slow)
        if fast is slow:
            break

    print()
    # means there's no loop as fast reached end of the list
    if fast is None or fast.next is None:
        print(fast)
        print(slow)
        return None

    print()
    # below code is to find the loop start point
    # slow starts from the start of the list and keep incrementing until it reaches where the loop start node
    slow = ll.head
    while fast is not slow:
        print(fast)
        print(slow)
        fast = fast.next  # fast continues moving by one through the loop
        slow = slow.next  # slow keeps incrementing until it reaches where the loop start node

    return fast


def test_loop_detection():
    looped_list = LinkedList(["A", "B", "C", "D", "E", "F", "G"])
    loop_start_node = looped_list.head.next.next.next  # the number of nodes down the list where the nodes start is
    # the same number of nodes from the tail of the list that the two runners will meet
    looped_list.tail.next = loop_start_node
    tests = [
        (LinkedList(), None),
        ((LinkedList((1, 2, 3))), None),
        (looped_list, loop_start_node),
    ]

    loop_detection(looped_list)
    loop_detection(LinkedList((1, 2, 3)))

    # for ll, expected in tests:
    #     assert loop_detection(ll) == expected


test_loop_detection()
