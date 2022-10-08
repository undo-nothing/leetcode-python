# Definition for singly-linked list.
class ListNode:

    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    '''
    反转链表
    反转一个单链表。

    示例:

    输入: 1->2->3->4->5->NULL
    输出: 5->4->3->2->1->NULL
    进阶:
    你可以迭代或递归地反转链表。你能否用两种方法解决这道题？
    '''

    def reverseList1(self, head: ListNode) -> ListNode:
        if not head:
            return head
        prev_node = None
        cur_node = head
        while cur_node.next:
            # 将下个节点设置成自身上一个节点
            next_node = cur_node.next
            cur_node.next = prev_node

            # 循环到下一个节点
            prev_node = cur_node
            cur_node = next_node

        cur_node.next = prev_node
        return cur_node

    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # 递归终止条件是当前为空，或者下一个节点为空
        # head is None 为了防止head.next判断的报错
        if head is None or head.next is None:
            return head
        # 这里的cur永远是最后一个节点，作为最终的返回值
        last_node = self.reverseList(head.next)
        # 将下下个节点设置成自身，自身下一个值设置成空，完成反转
        head.next.next = head
        # 防止链表循环，需要将head.next设置为空
        head.next = None
        # 每层递归函数都返回last_node
        return last_node


class Solution1:
    '''
    合并链表
    将两个有序链表合并为一个新的有序链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。 

    示例：

    输入：1->2->4, 1->3->4
    输出：1->1->2->3->4->4
    '''

    def mergeTwoLists1(self, l1: ListNode, l2: ListNode) -> ListNode:
        l3 = head = ListNode(0)
        while l1 and l2:
            if l1.val < l2.val:
                l3.next = l1
                l1 = l1.next
            else:
                l3.next = l2
                l2 = l2.next
            l3 = l3.next

        l3.next = l1 or l2
        return head.next

    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 is None and l2 is None:
            return None
        if l1 is None and l2 is not None:
            return l2
        if l1 is not None and l2 is None:
            return l1

        if l1.val > l2.val:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2
        else:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1


class Solution2:
    '''
    相交链表
    编写一个程序，找到两个单链表相交的起始节点。
    注意
    如果两个链表没有交点，返回 null.
    在返回结果后，两个链表仍须保持原有的结构。
    可假定整个链表结构中没有循环。
    程序尽量满足 O(n) 时间复杂度，且仅用 O(1) 内存。
    注意相等不定义为值相等，而是节点的地址相等
    '''

    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        # 两条不同的遍历路径，分别从a, b开始遍历
        # 当a遍历完后继续遍历b， 当b遍历完后继续遍历a
        # 当值第一次相等时，就是交点
        if not (headA and headB):
            return None
        pA, pB = headA, headB
        while pA != pB:
            pA = headB if pA is None else pA.next
            pB = headA if pB is None else pB.next
        return pA


class Solution3:
    '''
    环形链表
    给定一个链表，判断链表中是否有环。
    为了表示给定链表中的环，我们使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。 如果 pos 是 -1，则在该链表中没有环。

    示例 1：

    输入：head = [3,2,0,-4], pos = 1
    输出：true
    解释：链表中有一个环，其尾部连接到第二个节点。

    示例 2：

    输入：head = [1,2], pos = 0
    输出：true
    解释：链表中有一个环，其尾部连接到第一个节点。

    示例 3：

    输入：head = [1], pos = -1
    输出：false
    解释：链表中没有环。

    进阶：
    你能用 O(1)（即，常量）内存解决此问题吗？
    '''

    def hasCycle(self, head: ListNode) -> bool:
        if head is None or head.next is None:
            return False

        slow = head
        fast = head.next
        while slow != fast:
            if fast is None or fast.next is None:
                return False
            slow = slow.next
            fast = fast.next.next

        return True
