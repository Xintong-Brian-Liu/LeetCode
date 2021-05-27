'''
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Output: Because nums[0] + nums[1] == 9, we return [0, 1].

This version is returning index, so we cannot use two pointer and sort.

What we need is when there is a number in the list that equals to target - current, we return the indexs
So I need something to keep in track of that number and index. 
Then I think of dict. {" ":" "}

When the number is not in the dict, we store it like {"num" : "index", }
So when next time, if we found a match, we just can call dict[num] to get the index. 
'''

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for i in range(len(nums)):
            n = target - nums[i]
            if n not in dic.keys():
                dic[nums[i]] = i
            else:
                return (dic[n], i)