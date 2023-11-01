class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dic = {}
        max_len = start = 0

        for index, char in enumerate(s):
            if char in dic and start <= dic[char]:
                start = dic[char] + 1
            else:
                max_len = max(max_len,index - start + 1)
            
            dic[char] = index
        
        return max_len
 
