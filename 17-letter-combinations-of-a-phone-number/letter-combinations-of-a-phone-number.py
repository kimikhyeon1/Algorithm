class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits is "" :
            return []

        def DFS(number,x):    
            if len(x) == len(digits):
                answer.append(x)
                return
            
            for i in range(number,len(digits)):
                for j in dic[digits[i]]:
                    DFS(i+1,x+j)
        
        answer = []
        dic = { "2":"abc", "3":"def", "4":"ghi", "5":"jkl", "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz" }
        DFS(0,"")

        return answer




        