'''
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.


Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
'''
# Approach 1: Keep Track of zero and replace - O(n)

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero_pos = 0
        for i, ele in enumerate(nums):
            if ele != 0:
                nums[zero_pos], nums[i] = nums[i], nums[zero_pos]
                zero_pos += 1 # Keep increasing until its a zero, to track the position zero

# Approach 2: Remove the zero and add it to the end - O(n^2)
class Solution(object):
    def moveZeroes(self, nums):
        i = 0
        end = len(nums)
        while i < end:
            if nums[i] == 0:
                del nums[i] # Del cost one n
                nums.append(0)
                end -= 1
            else:
                i += 1