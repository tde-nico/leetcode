class Solution:
    def sortVowels(self, s: str) -> str:
        v = [i for i in s if i in 'AEIOUaeiou']
        if not v:
            return s
        
        v.sort()
        i = 0
        string = list(s)
        for j in range(len(string)):
            if string[j] in 'AEIOUaeiou':
                string[j] = v[i]
                i += 1

        return ''.join(string)