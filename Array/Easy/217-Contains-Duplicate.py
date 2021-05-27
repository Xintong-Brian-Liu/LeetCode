'''
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

Input: nums = [1,2,3,1]
Output: true

'''
# Approach 1 - sort and detect Time: O(nlogn)
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                return True
            else:
                continue
        return False

# Approach 2 - Heap Map - Time: o(n)

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashNum = {}
        for i in nums:
            if i not in hashNum:
                hashNum[i] = 1
            else:
                return True
        return False