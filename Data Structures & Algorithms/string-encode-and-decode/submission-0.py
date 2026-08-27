class Solution:

    def encode(self, strs: List[str]) -> str:
        size, res = [], ""
        for s in strs:
            size.append(len(s))
        for z in size:
            res += str(z)
            res += ','
        res += '#'
        for s in strs:
            res += s
        return res

    def decode(self, s: str) -> List[str]:
        if not s:
            return []
        size, res, i = [], [], 0
        while s[i] != '#':
            curr = ""
            while s[i] != ',':
                curr += s[i]
                i += 1
            size.append(int(curr))
            i += 1
        i += 1
        for z in size:
            res.append(s[i:i + z])
            i += z
        return res
