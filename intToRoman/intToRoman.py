class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        hashmap = {1000: 'M', 900: 'CM', 500: 'D', 400: 'CD', 100: 'C', 90: 'XC', 50: 'L', 40: 'XL', 10: 'X', 9: 'IX',
                   5: 'V', 4: 'IV', 1: 'I'}
        res = ''
        for key in hashmap:
            if num // key != 0:
                count = num // key
                res += hashmap[key] * count
                num %= key
        return res


if __name__ == '__main__':
    a = Solution()
    print(a.intToRoman(4))
