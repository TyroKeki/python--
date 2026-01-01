class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)

node1.next = node2
node2.next = node3
head1 = node1

def createNodeList(values):
    head = ListNode(values[0])
    current = head

    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next

    return head

"""使用示例"""
head2 = createNodeList([1,2,3,4,5])

def printNodeList(head):
    current = head
    result = []
    while current:
        result.append(current.val)
        current = current.next
    print("->".join(map(str,result)))

printNodeList(head1)
printNodeList(head2)
