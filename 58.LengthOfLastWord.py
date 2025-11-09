class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.rstrip()
        lastchar = s.rfind(" ")
        if lastchar == -1:
            return len(s)
        return len(s) - lastchar - 1