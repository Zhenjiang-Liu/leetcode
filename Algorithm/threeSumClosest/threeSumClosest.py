class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums = sorted(nums)
        length = len(nums)
        if length < 3:
            return None
        least_delta = nums[0] + nums[1] + nums[2] - target
        for i in range(length - 2):
            delta = nums[i] + nums[i+1] + nums[i+2] - target
            if delta > 0:
                if abs(delta) < abs(least_delta):
                    least_delta = delta
                continue
            delta = nums[i] + nums[length-2] + nums[length-1] - target
            if delta < 0:
                if abs(delta) < abs(least_delta):
                    least_delta = delta
                continue
            forward, backward = i + 1, length - 1
            delta = nums[i] + nums[forward] + nums[backward] - target
            while backward > forward:
                if delta == 0:
                    return target
                elif delta > 0:
                    backward -= 1
                else:
                    forward += 1
                if abs(delta) < abs(least_delta):
                    least_delta = delta
                delta = nums[i] + nums[forward] + nums[backward] - target
        return (target + least_delta)