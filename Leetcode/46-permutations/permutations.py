class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        def DFS(array):
            if len(array) == len(nums):
                answer.append(array[:])
                return
            
            for i in range(len(nums)):
                if nums[i] in array:
                    continue
                array.append(nums[i])
                DFS(array)
                array.pop()

        answer = []
        array = []
        DFS(array)
        return answer
