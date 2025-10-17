class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 1:
            return s

        biggest = s[0]

        def expand(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1:right]

        for i in range(len(s)):
            odd = expand(i, i)
            even = expand(i, i + 1)

            for candidate in (odd, even):
                if len(candidate) > len(biggest):
                    biggest = candidate

        return biggest

