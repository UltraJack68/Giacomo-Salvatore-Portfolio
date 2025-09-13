"""Given an array of non-negative integers arr, you are initially positioned at start index of the array. When you are at index i, you can jump to i + arr[i] or i - arr[i], check if you can reach any index with value 0.

Notice that you can not jump outside of the array at any time."""

class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        
        if arr[start] == 0:
            return True
        
        jumps = defaultdict(list)
        seen = set()
        queue = deque([start])
        
        for index in range(len(arr)):
            if arr[index] == 0:
                continue
            if index - arr[index] > -1:
                jumps[index].append(index - arr[index])
            if index + arr[index] < len(arr):
                jumps[index].append(index + arr[index])
                
        while queue:
                curr = queue.popleft()
                for jump in jumps[curr]:
                    if jump not in seen:
                        if arr[jump] == 0:
                            return True
                        seen.add(jump)
                        queue.append(jump)

        return False