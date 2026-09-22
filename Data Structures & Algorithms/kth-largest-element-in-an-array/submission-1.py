class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # nums.sort()
        # return nums[len(nums) - k]

        k = len(nums) - k

        def quickselect(l, r):
            pivot = nums[r]
            p = l
            for i in range(l, r):
                if nums[i] <= pivot:
                    nums[i], nums[p] = nums[p], nums[i]
                    p += 1
            nums[r], nums[p] = nums[p], nums[r]

            if p < k:
                return quickselect(p+1, r)
            elif p > k:
                return quickselect(l, p-1)
            else:
                return nums[p]

        return quickselect(0, len(nums)-1)