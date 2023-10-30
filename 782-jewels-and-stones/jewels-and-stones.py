class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        answer = 0
        for ch in jewels:
            for a in stones:
                if ch == a:
                    answer += 1

        return answer
        