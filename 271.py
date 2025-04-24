class Solution:

    def encode(self, strs: List[str]) -> str:
        extra = ''
        if len(strs):
            extra = '\0'
        return '\0'.join(strs) + extra

    def decode(self, s: str) -> List[str]:
        if s == "":
            return []
        return s.split('\0')[:-1]
