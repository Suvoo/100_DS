# Problem : https://practice.geeksforgeeks.org/problems/finding-middle-element-in-a-linked-list/1#

class Solution:
    #  Should return data of middle node. If linked list is empty, then  -1
    def findMid(self, head):
        
        if head is None: # Base 
            return -1

        temp = head
        nod = 0
        while temp:
            temp = temp.next
            nod+=1
        # temp is now Null here
        temp = head
        nod = nod//2
        while nod:
            temp = temp.next
            nod-=1
        return temp.data