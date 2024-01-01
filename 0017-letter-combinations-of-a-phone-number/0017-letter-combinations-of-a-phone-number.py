class Solution(object):
    def letterCombinations(self, digits):
        if not digits:
            return []

        digit_map = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        
        combinations = ['']
        for digit in digits:
            letters = digit_map[digit]
            combinations = [prefix + letter for prefix in combinations for letter in letters]
            
        return combinations