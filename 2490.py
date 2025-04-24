class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        i = 1
        l = len(sentence)-1
        if sentence[0] != sentence[-1]:
            return False
        while i < l:
            if sentence[i] == ' ' and sentence[i-1] != sentence[i+1]:
                    return False
            i += 1
        return True
