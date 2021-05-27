'''
Given a string s, find the length of the longest substring without repeating characters.

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

'''

# Approach - Window 
# Two pointer, the right pointer iterate the string
# Use the set to store the char if it not in set, if it is in set then, remove until it is the only one. 
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        left = 0
        res = 0
        for right in range(len(s)):
            while s[right] in charSet:
                charSet.remove(s[left])
                left += 1
            charSet.add(s[right])
            res = max(res, right - left + 1)
        return res
'''
0 0
{'p'}
0 1
{'p', 'w'}
2 2
{'w'}
2 3
{'k', 'w'}
2 4
{'k', 'e', 'w'}
3 5
{'k', 'w', 'e'}
'''
