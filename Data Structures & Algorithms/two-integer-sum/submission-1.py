class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_list = {}
        for i, num in enumerate(nums):
            k = target - num
            if k in nums_list:
                return [nums_list[k], i]
            nums_list[num] = i