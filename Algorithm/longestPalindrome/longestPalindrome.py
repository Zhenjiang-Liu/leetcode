class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if s == s[::-1]:
            return s
        res = s[:1]
        for i in range(len(s)):
            palindrome_odd = self.spread(s, i, i)
            palindrome_even = self.spread(s, i, i + 1)
            res = max(palindrome_odd, palindrome_even, res, key=len)
        return res

    def spread(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1:right]

