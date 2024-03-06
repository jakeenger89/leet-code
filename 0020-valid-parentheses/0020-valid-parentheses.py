class Solution(object):
    def isValid(self, s):
        mapping = {
            ')': '(',
            '}': '{',
            ']': '['
        }
        stack = []
        
        for char in s:
            if char in mapping:
                curr = stack.pop() if stack else 'happyman'
                if mapping[char] != curr:
                    return False
            else:
                stack.append(char)
        
        return not stack
        
        