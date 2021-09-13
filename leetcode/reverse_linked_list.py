# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Linked_List:
    def __init__(self):
        self.head = None

    def construct_linked_list(self, a):
        node = dummy =  ListNode()
        for i in a:
            node.next= ListNode(i) 
            node = node.next
        return dummy.next


    def print_list(self, node):
        value = node
        while value:
            print(value.val, end = ' ')
            value = value.next

    def reverseList(self, head: ListNode) -> ListNode:
        node = head
        l = []
        while node:
            l.append(node.val)
            node = node.next

        if len(l) <=1:
            return head

        head = ListNode(l[len(l)-1])
        node = head
        for i in range(len(l)-2, -1, -1):
            node.next = ListNode((l[i]))
            node = node.next
        return head

    def reverse_list_no_storage(self, head: ListNode):
        current = head
        prev = None
        while current:
            nextTemp = current.next
            current.next = prev
            prev = current
            current = nextTemp
        return prev

    def reverse_recursive(self, head: ListNode):
        if head == None or head.next == None:
            return head

        temp = self.reverse_recursive(head.next)
        head.next.next = head
        head.next = None
        return temp

a = [1,2,3,4,5]
# Output: [2,1]

# a = []
# Output: []
ll = Linked_List()
head = ll.construct_linked_list(a)
# new_head = ll.reverseList(head)
# new_head = ll.reverse_list_no_storage(head)
new_head = ll.reverse_recursive(head)
ll.print_list(new_head)