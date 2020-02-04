class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        l = nums1 + nums2
        l.sort()
        ln = len(l)
        if ln % 2 == 0:
            return (l[ln >> 1] + l[(ln >> 1) - 1]) / 2
        return l[ln >> 1]
