class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize:
            return False

        card_map = {}

        for h in hand:
            card_map[h] = 1 + card_map.get(h, 0)

        min_heap = list(card_map.keys())
        heapq.heapify(min_heap)

        while min_heap:
            first = min_heap[0]

            for i in range(first, first + groupSize):
                if i not in card_map.keys():
                    return False
                card_map[i] -= 1
                if card_map[i] == 0:
                    if i != min_heap[0]:
                        return False
                    heapq.heappop(min_heap)
        return True    