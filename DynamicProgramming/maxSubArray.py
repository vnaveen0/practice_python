class SolutionWrong(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        len_nums = len(nums)

        if len_nums == 1:
            return nums[0]

        i = 0
        prev_sum = nums[i]
        maxval = [prev_sum, 0, 0]
        j = 1
        cur_sum = prev_sum + nums[j]
        if cur_sum >= prev_sum:
            maxval = [cur_sum, i, j]

        def update_max(maxval, cur_sum, i, j):
            if maxval[0] <= cur_sum:
                maxval[0] = cur_sum
                maxval[1] = i
                maxval[2] = j
            return maxval, cur_sum

        while i < len_nums and j < len_nums and i <= j:
            if prev_sum == cur_sum:
                update_max(maxval, cur_sum, i, j)
                j += 1
                cur_sum = prev_sum + nums[j]
                maxval, cur_sum = update_max(maxval, cur_sum, i, j)

            # Check
            elif cur_sum >= prev_sum:
                j += 1
                if j < len_nums:
                    prev_sum = cur_sum
                    cur_sum = prev_sum + nums[j]
                    maxval, cur_sum = update_max(maxval, cur_sum, i, j)
                else:
                    j -= 1
                    break
            else:
                cur_sum = cur_sum - nums[i]
                prev_sum = cur_sum
                i += 1
                maxval, cur_sum = update_max(maxval, cur_sum, i, j)

        while i <= j:
            cur_sum = cur_sum - nums[i]
            i += 1
            maxval, cur_sum = update_max(maxval, cur_sum, i, j)

        print('-----')
        print(maxval)
        return maxval[0]

# Brute Force approach
class Solution1(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        def update_maxval(maxval, val, i, j):
            print('maxval: {}  val:{} i:{} j:{}'.format(maxval, val, i, j))
            if maxval is not None:
                if maxval[0] <= val:
                    maxval = [val, i, j]
            else:
                maxval = [val, i, j]
            return maxval

        len_nums = len(nums)
        maxval = None
        for i in range(len_nums):
            for j in range(i, len_nums):
                if i == j:
                    prev_sum = nums[i]
                    maxval = update_maxval(maxval, prev_sum, i, j)
                else:
                    cur_sum = prev_sum + nums[j]
                    maxval = update_maxval(maxval, cur_sum, i, j)
                    prev_sum = cur_sum

        return maxval[0]

# Dynamic Programming Solution 
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        len_nums = len(nums)
        prev_max = nums[0]
        cur_max = nums[0]

        for i in range(1, len_nums):
            cur_max = max(cur_max + nums[i], nums[i])
            prev_max = max(prev_max, cur_max)
        return prev_max