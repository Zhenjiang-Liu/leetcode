class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        return max(min(int(*re.findall('^[\+\-]?\d+', str.lstrip())), 2**31 - 1), -2**31)