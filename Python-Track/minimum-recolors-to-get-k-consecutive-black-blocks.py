class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        s=blocks
        n=len(blocks)
        initial = Counter(s[:k])
        _min = initial["W"]
        if n == 1 and s == "W":
            _min = 1
        for j in range(n-k+1):
            if (j+k) <= n-1:
                if s[j+k] == "W":
                    initial['W'] += 1
            else:
                break
            if s[j] == 'W':
                initial['W'] -= 1
            _min = min(_min, initial['W'])
        return _min