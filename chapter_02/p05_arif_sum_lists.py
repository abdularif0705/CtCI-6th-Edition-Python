from linked_list import LinkedList


def sum_linked_list(n1, n2, carry):
    """ adds lists numbers in backwards order so 7->1->6-> + 5->9->2
    represents 617 + 295 and we should get the answer 912 """
    # ll_a,ll_b = ll_a.head,ll_b.head
    total = n1.value + n2.value + carry
    print(total)

    if total > 9:
        carry = 1
    else:
        carry = 0
    total = total % 10
    sum_list.append(total)
    print(total)
    # print(n1.next)
    if n1.next or n2.next is not None:
        if n1.next is None:
            n1.next.value = 0
            ll_a.add_multiple([0])
        elif n2.next is None:
            # n2.next.value = 0
            ll_b.add_multiple([0])
        sum_linked_list(n1.next, n2.next, carry)
    else:
        print(sum_list)
        sum_list.reverse()
        print(sum_list)
        # TODO: reverse list and convert to int and send back, fix code below
        sum_str = ''.join(map(str, sum_list))  # map turns everything in my lost into a str and join() concatenates
        # them # [str(x) for x in sum_list]
        print(sum_str)
        sum_int = int(sum_str)


def sum_linked_list_followup(ll_c, ll_d):
    """ adds lists numbers in normal order so 7->1->6->1 + 5->9->2
    represents 7161 + 592 and we should get the answer 7753 """
    # Pad the shorter list with zeros, this way we are looking at the lists in the right order so the 0's are added
    # to the Front of the shorter list to match it to the length of the bigger one
    if len(ll_c) < len(ll_d):
        for i in range(len(ll_d) - len(ll_c)):
            ll_c.add_to_beginning(0)
    else:
        for i in range(len(ll_c) - len(ll_d)):
            ll_d.add_to_beginning(0)

    n1, n2 = ll_c.head, ll_d.head
    result = 0

    while n1 and n2:
        result = (result * 10) + n1.value + n2.value
        n1 = n1.next
        nd = n2.next

    # Create new linked list
    ll = LinkedList()
    ll.add_multiple([int(i) for i in str(result)])

    return ll


def main():
    global ll_a
    ll_a = LinkedList()
    ll_a.add_multiple([7, 1, 6, 1])
    global ll_b
    ll_b = LinkedList()
    ll_b.add_multiple([5, 9, 2])
    global sum_list
    sum_list = list()
    carry = 0


    print("ll_a:", ll_a)
    print("ll_b:", ll_b)
    print("sum_linked_list(ll_a.head, ll_b.head, carry) prints: ")
    sum_linked_list(ll_a.head, ll_b.head, carry)

    ll_c = LinkedList()
    ll_c.add_multiple([7, 1, 6, 1])
    ll_d = LinkedList()
    ll_d.add_multiple([5, 9, 2])
    print("\n")
    print("ll_c:", ll_c)
    print("ll_d:", ll_d)
    print("sum_linked_list_followup(ll_c, ll_d) returns:", sum_linked_list_followup(ll_c, ll_d))
    # # ll_a = LinkedList()
    # ll_a.generate(4, 0, 9)
    # # ll_b = LinkedList()
    # ll_b.generate(3, 0, 9)
    # print(ll_a)
    # print(ll_b)
    # sum_linked_list(ll_a, ll_b,carry)
    # print(sum_linked_list_followup(ll_a, ll_b))


main()
