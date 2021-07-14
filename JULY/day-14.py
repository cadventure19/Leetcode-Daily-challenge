class Solution:
    def customSortString(self, order: str, SortString: str) -> str:
        
        
        orderMap=collections.defaultdict(lambda: 26)
        for index, c in enumerate(order):
            orderMap[c]=index
        
        return "".join(sorted(list(SortString),key=lambda c: orderMap[c]))