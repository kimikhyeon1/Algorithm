class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        array = deque()
        answer = 0
        target = 0

        while target < len(s):
            if s[target] in array:
                answer = max(answer, len(array))
                array.popleft()
                continue
            
            array.append(s[target])
            target += 1

        return max(answer, len(array))


