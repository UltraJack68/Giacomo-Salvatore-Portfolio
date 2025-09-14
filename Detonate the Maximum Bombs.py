"""You are given a list of bombs. The range of a bomb is defined as the area where its effect can be felt. This area is in the shape of a circle with the center as the location of the bomb.

The bombs are represented by a 0-indexed 2D integer array bombs where bombs[i] = [xi, yi, ri]. xi and yi denote the X-coordinate and Y-coordinate of the location of the ith bomb, whereas ri denotes the radius of its range.

You may choose to detonate a single bomb. When a bomb is detonated, it will detonate all bombs that lie in its range. These bombs will further detonate the bombs that lie in their ranges.

Given the list of bombs, return the maximum number of bombs that can be detonated if you are allowed to detonate only one bomb."""

class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        hashmap = defaultdict(list)
        n = -1
        Max = 1
        
        for index in range(len(bombs)):
            bombs[index].append(index)
                     
            
        for bomb in bombs:
            for other_bomb in bombs:
                if other_bomb == bomb:
                    continue
                if bomb[2] >= (((bomb[0] - other_bomb[0])**2) + (bomb[1] - other_bomb[1])**2)**0.5:
                    hashmap[bomb[3]].append(other_bomb[3])
                    
        for bomb in hashmap:
            queue = deque([bomb])
            seen = {bomb}
            while queue:
                curr = queue.popleft()
                if curr in hashmap:    
                    for closeby in hashmap[curr]:
                        if closeby not in seen:
                            seen.add(closeby)
                            queue.append(closeby)
            Max = max(Max, len(seen))
            
        return Max