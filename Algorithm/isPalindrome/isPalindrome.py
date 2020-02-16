class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        revnum = 0
        while(x>revnum):
            revnum = revnum*10 + x % 10
            x = x//10
        return x == revnum or x == revnum//10

    def isPalindrome1(self, x):
        """
        :type x: int
        :rtype: bool
        """
        x = str(x)
        return x == x[::-1]