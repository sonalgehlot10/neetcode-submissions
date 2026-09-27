class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        currMax = 1
        currMin = 1

        for num in nums:
            temp = currMax * num
            currMax = max(
                num,
                currMax * num,
                currMin * num
            )
            currMin = min(
                num,
                temp,
                currMin * num
            )
            res = max(res, currMax)
        return res

# Time: O(n)
# Space: O(1)