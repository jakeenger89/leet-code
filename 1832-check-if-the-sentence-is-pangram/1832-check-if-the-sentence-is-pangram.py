import string
class Solution(object):
    def checkIfPangram(self, sentence):
        alphabet = set(string.ascii_lowercase)
        sentence = sentence.lower()
        sentence_chars = set(sentence)
        sentence_chars.discard('')
        return set(alphabet) <= sentence_chars