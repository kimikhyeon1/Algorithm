class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = {}
        array = []
        for nums in nums:
            if nums in dic:
                dic[nums] += 1
            else:
                dic[nums] = 1
        
        for key,value in dic.items():
            array.append([value,key])
        
        array.sort(reverse=True)
        answer = []

        for i in range(k):
            answer.append(array[i][1])
 
        
        return sorted(answer)