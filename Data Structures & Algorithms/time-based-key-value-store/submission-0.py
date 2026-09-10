class TimeMap:

    def __init__(self):
        self.store = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        
        pairs = self.store[key]

        l = 0
        r = len(pairs) - 1
        res = ""

        while l <= r:
            m = (l+r) // 2

            if pairs[m][0] == timestamp:
                res = pairs[m][1]
                return res
            elif pairs[m][0] < timestamp:
                res = pairs[m][1]
                l = m + 1
            else:
                r = m - 1
        return res
            