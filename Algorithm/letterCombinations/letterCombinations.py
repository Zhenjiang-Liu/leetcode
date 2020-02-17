class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits: return []

        phone = {'2': ['a', 'b', 'c'],
                 '3': ['d', 'e', 'f'],
                 '4': ['g', 'h', 'i'],
                 '5': ['j', 'k', 'l'],
                 '6': ['m', 'n', 'o'],
                 '7': ['p', 'q', 'r', 's'],
                 '8': ['t', 'u', 'v'],
                 '9': ['w', 'x', 'y', 'z']}

        def backtrack(conbination, nextdigit):
            if not nextdigit.__len__():
                res.append(conbination)
            else:
                keys = nextdigit[0]
                for letter in phone[keys]:
                    backtrack(conbination + letter, nextdigit[1:])

        res = []
        backtrack('', digits)
        return res


if __name__ == '__main__':
    a = Solution()
    res = a.letterCombinations("23")
    print(res)
