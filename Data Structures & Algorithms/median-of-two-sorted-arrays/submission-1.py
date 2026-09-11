class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A = nums1
        B = nums2
        Total = len(nums1) + len(nums2)
        Half = Total // 2

        if len(A) > len(B):
            A, B = B, A

        l = 0
        r = len(A) - 1

        while True:
            i = (l+r) // 2
            j = Half - i - 2

            Aleft = A[i] if i >= 0 else float("-inf")
            Aright = A[i + 1] if (i+1) < len(A) else float("inf")
            Bleft = B[j] if j >= 0 else float("-inf")
            Bright = B[j + 1] if (j+1) < len(B) else float("inf")

            if Aleft <= Bright and Bleft <= Aright:
                if Total % 2 == 1:
                    return min(Aright, Bright)
                return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
            elif Bleft > Aright:
                l = i + 1
            else:
                r = i - 1

# Time: log(min(m,n))
# Space: O(1)
