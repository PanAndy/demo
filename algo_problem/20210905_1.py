
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:

    def solve(self, a):
        ret = None
        head = None
        while True:
            flag = False

            for i in range(len(a)):
                if head is None and a[i] is not None:
                    head = a[i]
                    ret = a[i]
                    a[i] = a[i].next
                    flag = True
                    continue

                if a[i] is not None and ret is not None:
                    ret.next = a[i]
                    ret = ret.next
                    flag = True
                if a[i] is not None:
                    a[i] = a[i].next
            if flag is False:
                break

        return head


def print_(a):
    item = a
    while item is not None:
        print(item.val)
        item = item.next


if __name__ == "__main__":
    a1 = ListNode(1)
    a2 = ListNode(2)
    a3 = ListNode(3)

    b1 = ListNode(4)
    b2 = ListNode(5)

    c1 = ListNode(7)
    c2 = ListNode(8)
    c3 = ListNode(9)
    c4 = ListNode(10)
    c5 = ListNode(11)
    c6 = ListNode(12)

    a1.next = a2
    a2.next = a3

    b1.next = b2

    c1.next = c2
    c2.next = c3
    c3.next = c4
    c4.next = c5
    c5.next = c6

    a = [a1, b1, c1]

    sol = Solution().solve(a)
    print_(sol)



