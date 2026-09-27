class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def dfs(i, cur, total):
            if total == target:
                res.append(cur.copy())
                return
            if i >= len(nums) or total > target:
                return

            cur.append(nums[i])
            dfs(i, cur, total + nums[i])
            cur.pop()
            
            dfs(i + 1, cur, total)
                
        dfs(0, [], 0)
        return res

# Time: O(2^t/m) {because we make two choices (include or skip) at each step up to a maximum recursion depth of t/m} 

# Space: O(t/m) {because that maximum depth is the longest combination path temporarily stored in memory}