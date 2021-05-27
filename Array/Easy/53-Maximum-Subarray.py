'''
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
'''

# Approach 1 Brute Force:
#    Since we only need to find the max_sum, not the exact array, we can use a second pointer so we keep adding and replace the current_max

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = -math.inf
        for i in range(len(nums)):
            current_sum = 0
            for j in range(i, len(nums)):
                current_sum += nums[j]
                max_sum = max(max_sum, current_sum)

        return max_sum

#    !! However, this solution it overtime for some reason. 

#    Whenever you see q question that asks for the maximum or minimum of something, consider DP (Q121)

# Approach 2 DP:

#    DP could dynamically change the max or min sum of something 

#    Here we need to find the max sum of a certain array. 
#    So we update the current_sum by max(current_sum, current_sum+num)
#    And keep track of max_sum by max(current_sum, max_sum) to update the max

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Initialize our variables using the first element.

        current_subarray = max_subarray = nums[0]
        
        # Start with the 2nd element since we already used the first one.
        for num in nums[1:]:
            # If current_subarray is negative, throw it away. Otherwise, keep adding to it.
            # Once the max reachs the max, it stays there. 
            
            current_subarray = max(num, current_subarray + num)
            max_subarray = max(max_subarray, current_subarray)
        
        return max_subarray

# Approach 3: Greedy 

#   If the current_sum < 0 and current_num > 0, then we can swap
#   Else we add them together 
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums: return 0

        current_sum = nums[0]
        max_sum = current_sum
        i = 1
        
        while i < len(nums):
            current_num = nums[i]
            if current_sum <= 0 and current_num > 0:
                current_sum = current_num
            else:
                current_sum += current_num
        
            max_sum = max(current_num, current_sum, max_sum)
            i += 1
        return max_sum

