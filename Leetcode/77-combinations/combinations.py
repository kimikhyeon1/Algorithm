class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        answer = []
        def combinations(index,array):
            if len(array) == k:
                answer.append(array[:])
                return
            
            for i in range(index,n+1):
                if index in array:
                    continue
                array.append(i)
                combinations(i+1,array)
                array.pop()
            
        combinations(1,[])
        return answer


        