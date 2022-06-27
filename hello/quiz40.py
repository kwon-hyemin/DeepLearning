import heapq
class Quiz40:
    def quiz40(self ,scoville, K):
        heapq.heapify(scoville)
        count = 0
        while len(scoville) >= 2 and scoville[0] < K:
            fist, second = heapq.heappop(scoville), heapq.heappop(scoville)
            heapq.heappush(scoville, fist+(second*2))
            count += 1
        return count if scoville[0] >= K else-1


    def quiz41(self) -> str: return None

    def quiz42(self) -> str: return None

    def quiz43(self) -> str: return None

    def quiz44(self) -> str: return None

    def quiz45(self) -> str: return None

    def quiz46(self) -> str: return None

    def quiz47(self) -> str: return None

    def quiz48(self) -> str: return None

    def quiz49(self) -> str: return None