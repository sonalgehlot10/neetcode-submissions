class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        charset = set()
        l = 0

        for r in range(len(s)):
            while s[r] in charset:
                charset.remove(s[l])
                l += 1
            charset.add(s[r])
            longest = max(longest, r - l + 1)
        return longest

# Time: O(n) {length of string s}
# Space: O(m) {total unique characters in s}