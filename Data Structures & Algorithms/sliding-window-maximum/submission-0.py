class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output = []
        l = 0
        r = 0
        dq = collections.deque()

        while r < len(nums):
            while dq and nums[r] > nums[dq[-1]]:
                dq.pop()
            dq.append(r)

            if l > dq[0]:
                dq.popleft()

            if (r + 1) >= k:
                output.append(nums[dq[0]])
                l += 1
            r += 1
        return output