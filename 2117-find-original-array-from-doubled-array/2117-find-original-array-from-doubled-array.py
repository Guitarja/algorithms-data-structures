class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        changed.sort()
        heap = []
        ret = []
        for num in changed:
            if heap and heap[0]*2 == num:
                ret.append(heapq.heappop(heap))
            else:
                heapq.heappush(heap, num)
        
        return ret if not heap else []
