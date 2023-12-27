class Solution(object):
    
    def isValid(self, s):
        stack = []
        character = {')': '(', '}': '{', ']': '['}

        for char in s:
            if char in character.values():
                stack.append(char)
            elif char in character:
                if not stack or stack.pop() != character[char]:
                    return False
            else:
                return False

        return not stack