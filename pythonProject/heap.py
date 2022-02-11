import heapq
maxheap=[]
heapq.heapify(maxheap)
heapq.heappush(maxheap,-1*1)
heapq.heappush(maxheap,-1*2)
heapq.heappush(maxheap,-1*3)
print("maxHeap: ", maxheap)
peekNum = maxheap[0]
print("peek number:",-1*maxheap[0])



