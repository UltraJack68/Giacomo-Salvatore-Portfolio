"""A gene string can be represented by an 8-character long string, with choices from 'A', 'C', 'G', and 'T'.

Suppose we need to investigate a mutation from a gene string startGene to a gene string endGene where one mutation is defined as one single character changed in the gene string.

For example, "AACCGGTT" --> "AACCGGTA" is one mutation.
There is also a gene bank bank that records all the valid gene mutations. A gene must be in bank to make it a valid gene string.

Given the two gene strings startGene and endGene and the gene bank bank, return the minimum number of mutations needed to mutate from startGene to endGene. If there is no such a mutation, return -1.

Note that the starting point is assumed to be valid, so it might not be included in the bank."""

class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        hashmap = defaultdict(set)
        queue = deque([startGene])
        bank.append(startGene)
        seen = set()
        diff = 0
        ans = 0
        
        if endGene == startGene:
            return 0
        
        for gene in bank:
            for other in bank:
                if other == gene:
                    continue
                else:
                    diff = 0
                    for letter1, letter2 in zip(gene, other):
                        if letter1 != letter2:
                            if diff == 0:
                                diff = 1
                            else:
                                diff = 2
                                break
                    if diff == 1:
                        hashmap[gene].add(other)
                        hashmap[other].add(gene)

        while queue:
            ans += 1
            for _ in range(len(queue)):
                curr = queue.popleft()
                for element in hashmap.get(curr, set()):  # iterate over the set
                    if element == endGene:
                        return ans
                    if element not in seen:
                        seen.add(element)
                        queue.append(element)
                        
        return -1