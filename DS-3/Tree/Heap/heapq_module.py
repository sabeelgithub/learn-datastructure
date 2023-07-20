import heapq

heap = []
print(heapq)
heapq.heappush(heap,5)
heapq.heappush(heap,15)
heapq.heappush(heap,10)
heapq.heappush(heap,20)
print(heap)
print(heapq.heappop(heap))
print(heapq.heappop(heap))
print(heap)
list = [2,9,0,6,8,9]
heapq.heapify(list)
print(list)
heapq.heappush(list,10)
print(list)
heapq.heappushpop(list,11)
print(list)
heapq.heapreplace(list,12)
print(list)
print(heapq.nsmallest(2,list))
print(heapq.nlargest(2,list))
