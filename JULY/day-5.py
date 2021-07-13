class Solution(object):
    def minSetSize(self, arr):
        length=len(arr)
        dic={}
        for i in arr:
            if i in dic:
                dic[i]+=1
            else:
                dic[i]=1
        count=0
        total=length
        for i in reversed(sorted (dic.values())):
            total-=i
            count+=1
            if total<=length//2:
                break
        return count