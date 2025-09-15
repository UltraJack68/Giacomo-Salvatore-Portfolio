"""A transformation sequence from word beginWord to word endWord using a dictionary wordList is a sequence of words beginWord -> s1 -> s2 -> ... -> sk such that:

Every adjacent pair of words differs by a single letter.
Every si for 1 <= i <= k is in wordList. Note that beginWord does not need to be in wordList.
sk == endWord
Given two words, beginWord and endWord, and a dictionary wordList, return the number of words in the shortest transformation sequence from beginWord to endWord, or 0 if no such sequence exists."""

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        L = len(beginWord)

        patterns = defaultdict(list)
        for word in wordList:
            for i in range(L):
                patterns[word[:i] + "*" + word[i+1:]].append(word)

        queue = deque([(beginWord, 1)])
        seen = set([beginWord])

        while queue:
            word, steps = queue.popleft()
            if word == endWord:
                return steps
            for i in range(L):
                pattern = word[:i] + "*" + word[i+1:]
                for neighbor in patterns[pattern]:
                    if neighbor not in seen:
                        seen.add(neighbor)
                        queue.append((neighbor, steps + 1))
                patterns[pattern] = []
        
        return 0