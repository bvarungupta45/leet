class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        dic={}
        for i in arr:
            if i not in dic:
                dic[i]=1
            else:
                dic[i]+=1
        if len(set(list(dic.values())))==len(list(dic.values())):
            return True
        else:
            return False
            