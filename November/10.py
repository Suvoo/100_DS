# Take : 
# 1. Find Middle 
# 2.Reverse from next of middle 
# 3. Compare

#Function to check whether the list is palindrome.
class Solution:
    def isPalindrome(self, head):
        #code here
        def FindMid(head):
            slow = head
            fast = head.next
            while fast!=None and fast.next != None:
                fast = fast.next.next
                slow = slow.next
            return slow

        def Rev(head):
            prev = None
            curr = head
            nextt = None
            
            while curr != None:
                nextt = curr.next
                curr.next = prev
                prev = curr
                curr = nextt
            return prev
        if head.next == None: 
            return True

        middle =  FindMid(head)
        # print(middle.data)
        rightHead = Rev(middle.next)
        # print(rightHead.data)

        while head != None and rightHead != None:
            if head.data != rightHead.data:
                return False
            head = head.next
            rightHead = rightHead.next
        return True