# https://leetcode.com/problems/merge-two-sorted-lists/


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1,list2) :
        if list1 is None :
            return list2
        elif list2 is None :
            return list1
        
        p1 = list1
        p2 = list2
        
        if p1.val < p2.val :
            head = p1
            current = head
            p1 = p1.next
        else :
            head = p2
            current = head
            p2 = p2.next
        
        while True :
            #print(p1.val, p2.val, getArr(head), getArr(current))
            if p1 == None :
                current.next = p2
                return head
            if p2 == None :
                current.next = p1
                return head
            
            if p1.val < p2.val :
                current.next = p1
                p1 = p1.next
            else :
                current.next = p2
                p2 = p2.next
                
            current = current.next
            
                

def getArr(linked) :
    arr = []
    while linked != None :
      arr.append(linked.val)
      linked = linked.next
    return arr        
            
