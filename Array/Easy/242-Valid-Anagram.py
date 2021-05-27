'''
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

'''

# Approach 1:
# We can just test to see whether it is the same after sorted
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if(len(s) != len(t)): return False
        return sorted(s) == sorted(t)

# Approach 2:
# We can use a dictionary to store the char and the frequence of that char
# If that frequency is not zero at the end, then it is false. 

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dic = {}
        for char in s:
            if char not in dic:
                dic[char] = 1
            else:
                dic[char] += 1

        for char in t:
            if char not in dic:
                return False
            else:
                dic[char] -= 1
        
        for val in dic.values():
            if val != 0:
                return False
            
        return True