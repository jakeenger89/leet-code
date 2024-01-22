class Solution(object):
    def wordPattern(self, pattern, s):
        words = s.split()
        
        if len(pattern) != len(words):
            return False
        
        patterntoWord = {}
        wordtoPattern = {}
        
        for char, word in zip(pattern, words):
            if char in patterntoWord:
                if patterntoWord[char] != word:
                    return False
            else:
                patterntoWord[char] = word
            
            if word in wordtoPattern:
                if wordtoPattern[word] != char:
                    return False
            else:
                wordtoPattern[word] = char
        return True
        