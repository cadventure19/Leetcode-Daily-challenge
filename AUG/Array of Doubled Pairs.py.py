class Solution:
    def canReorderDoubled(self, arr: List[int]) -> bool:
        count=collections.Counter()
        # print(count)
        for x in sorted(arr, key=lambda x: abs(x), reverse=True):
            if count[x*2]>0:
                count[x*2]-=1
                
            else:
                count[x]+=1
        return sum(count.values())==0

print(Solution())