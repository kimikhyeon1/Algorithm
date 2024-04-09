class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = [0] * len(temperatures)

        stack = []

        for i, val in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < val:
                cur = stack.pop()
                answer[cur] = i - cur
            
            stack.append(i)

        return answer

