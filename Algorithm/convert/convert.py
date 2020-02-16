class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows < 2:
            return s
        res = ["" for i in range(numRows)]
        start, flag = 0, -1
        for c in s:
            res[start] += c
            if start == 0 or start == numRows - 1:
                flag = -flag
            start += flag
        return "".join(res)