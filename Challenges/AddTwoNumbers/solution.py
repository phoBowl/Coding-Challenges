#!/usr/bin/python3

# https://leetcode.com/problems/add-two-numbers/description/
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummyHead = ListNode(0)
        curr = dummyHead
        curr1 = l1
        curr2 = l2
        carry = 0
        tempCurr1 = tempCurr2 = None
        while(curr1 != None or curr2 != None):
            tempCurr1 = curr1.val if curr1 != None else 0
            tempCurr2 = curr2.val if curr2 != None else 0 
            
            sum = tempCurr1 + tempCurr2 + carry
            carry = sum / 10
            curr.next = ListNode(sum % 10)
            curr = curr.next
            
            if curr1 != None: curr1 = curr1.next 
            if curr2 != None: curr2 = curr2.next 
            
        if( carry > 0 ):
            curr.next = ListNode(carry)
            
        return dummyHead.next

