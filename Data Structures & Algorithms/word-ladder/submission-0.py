from collections import defaultdict, deque
from typing import List


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        word_set = set(wordList)
        if endWord not in word_set:
            return 0
        if beginWord == endWord:
            return 1

        # Map each wildcard pattern (e.g. "*ot") -> words in wordList matching it
        pattern_to_words = defaultdict(list)
        for word in word_set:
            for i in range(len(word)):
                pat = word[:i] + "*" + word[i + 1 :]
                pattern_to_words[pat].append(word)

        q = deque()
        visited_patterns = set()
        visited_words = {beginWord}

        # Seed the queue with all wildcard patterns of beginWord
        for i in range(len(beginWord)):
            pat = beginWord[:i] + "*" + beginWord[i + 1 :]
            if pat not in visited_patterns:
                visited_patterns.add(pat)
                q.append(pat)

        # beginWord is word #1; after finishing layer 1 of patterns, we reach words at length 2
        count = 1

        while q:
            count += 1
            layer_size = len(q)

            for _ in range(layer_size):
                pat = q.popleft()

                for word in pattern_to_words[pat]:
                    if word == endWord:
                        return count

                    if word in visited_words:
                        continue
                    visited_words.add(word)

                    # Look up next wildcard patterns for this word
                    for i in range(len(word)):
                        next_pat = word[:i] + "*" + word[i + 1 :]
                        if next_pat not in visited_patterns:
                            visited_patterns.add(next_pat)
                            q.append(next_pat)

        return 0