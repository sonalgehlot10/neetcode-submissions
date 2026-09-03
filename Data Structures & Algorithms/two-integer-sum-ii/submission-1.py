class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        numset = {}
        for i , num in enumerate(numbers):
            diff = target - num
            if diff in numset:
                return [numset[diff]+1, i+1]
            numset[num] = i
            