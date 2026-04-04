class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapq.heapify_max(stones)

        while len(stones) > 1:
            max_1 = heapq.heappop_max(stones)
            max_2 = heapq.heappop_max(stones)
            
            print(max_1, max_2)

            if max_1 == max_2:
                continue
            push_val = max_1 - max_2
            
            heapq.heappush_max(stones, push_val)
        if len(stones) <= 0:
            return 0
        max_item = heapq.heappop_max(stones)
        return max_item