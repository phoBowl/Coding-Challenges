#!/usr/bin/python3

# https://leetcode.com/problems/two-sum/description/
class Solution(object):
    def twoSum(self, nums, target):
        my_dict = dict()
        for counter, num in enumerate(nums):
            print(counter, num)
            diff = target - num
            if diff in my_dict:
                return my_dict[diff], counter
            my_dict[num] = counter

