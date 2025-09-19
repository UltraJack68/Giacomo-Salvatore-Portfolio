"""Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane and an integer k, return the k closest points to the origin (0, 0).

The distance between two points on the X-Y plane is the Euclidean distance (i.e., √(x1 - x2)2 + (y1 - y2)2).

You may return the answer in any order. The answer is guaranteed to be unique (except for the order that it is in)."""

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = [[(x**2 + y**2), [x, y]] for x, y in points]
        heapify(distances)
        ans = []
        
        for _ in range(k):
            curr = heappop(distances)
            ans.append(curr[1])
            
        return ans