class Solution:
    def minWindow(self, s: str, t: str) -> str:
        countT = {}
        window = {}
        for c in t:
            countT[c] = 1 + countT.get(c, 0)
        
        have = 0
        need = len(countT)

        l = 0

        res = ""
        reslen = float("inf")

        for r in range(len(s)):
            window[s[r]] = 1 + window.get(s[r], 0)

            if s[r] in countT and countT[s[r]] == window[s[r]]:
                have += 1

            while have == need:
                if reslen > r - l + 1:
                    reslen = min(reslen, r - l + 1)
                    res = s[l : r + 1]
                window[s[l]] -= 1
                if s[l] in countT and countT[s[l]] > window[s[l]]:
                    have -= 1
                l += 1
        return res

