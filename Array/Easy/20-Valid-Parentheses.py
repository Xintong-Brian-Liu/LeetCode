'''
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.

Input: s = "()[]{}"
Output: true

Input: s = "{[]}"
Output: true

Input: s = "([)]"
Output: false
'''

# 有两种case，第一种就是input1中，相邻的两个parentheses，这样当发现不是opening的时候，就直接pop
# 第二种就是后两个input中，中间穿插别的bracket，最里面的那个一定是对称的，那么我们利用stack的pop（）LIFO的思路直接进行比较
# 如果当前的char是这个opening的closing则继续，
class Solution:
    def isValid(self, s: str) -> bool:
        dic = {"(":")", "{":"}", "[":"]"}
        # List to store the char when it is opening. 
        lst = []
        for char in s:
            if char in dic.keys():
                lst.append(char)
            elif not lst:
                return False
            else:
                # Get the opening and supposed closing
                openning = lst.pop()
                closing = dic[openning]
                # Check if current char is the closing
                if char != closing:
                    return False
        return not lst