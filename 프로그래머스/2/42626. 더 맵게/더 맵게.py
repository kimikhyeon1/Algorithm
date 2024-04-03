import heapq
def solution(scoville, K):
    count = 0
    scoville.sort()

    if scoville[0] >= K:
        return 0

    while K > scoville[0]:
        if len(scoville) == 1:
            break
        new_scoville = heapq.heappop(scoville) + (heapq.heappop(scoville) * 2)
        heapq.heappush(scoville, new_scoville)
        count += 1

    if scoville[0] < K:
        return -1
    
    return count