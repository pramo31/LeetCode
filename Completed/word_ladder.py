from collections import deque
from typing import List
from typing import Dict

"""
Given two words (beginWord and endWord), and a dictionary's word list, find the length of shortest transformation sequence from beginWord to endWord, such that:

Only one letter can be changed at a time.
Each transformed word must exist in the word list. Note that beginWord is not a transformed word.
Note:

Return 0 if there is no such transformation sequence.
All words have the same length.
All words contain only lowercase alphabetic characters.
You may assume no duplicates in the word list.
You may assume beginWord and endWord are non-empty and are not the same.
"""


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if (endWord not in wordList):
            return 0
        else:
            nodeEdgeDict = {}
            for word in wordList:
                for i in range(0, len(word)):
                    temp = word[0:i] + "*" + word[i + 1:]
                    if (temp in nodeEdgeDict.keys()):
                        nodeEdgeDict[temp].append(word)
                    else:
                        nodeEdgeDict[temp] = [word]
            visited = set()
            queue = deque()
            queue.append((beginWord, 1))
            while (queue):
                node = queue.popleft()
                word = node[0]
                level = node[1]
                if (word == endWord):
                    return level
                if (word not in visited):
                    visited.add(word)
                    lst = [(word[0:i] + "*" + word[i + 1:]) for i in range(0, len(word))]
                    children = []
                    for exp in lst:
                        if (exp in nodeEdgeDict.keys()):
                            children += nodeEdgeDict[exp]
                    children = set(children) - visited
                    for child in children:
                        queue.append((child, level + 1))
            return 0


if (__name__ == "__main__"):
    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot", "dot", "dog", "lot", "log", "cog"]  # ["hot", "dot", "dog", "lot", "log", "cog"]
    # wordList = ["hot", "dot", "dog", "lot", "log"]

    obj = Solution()
    steps = obj.ladderLength(beginWord, endWord, wordList)
    if (steps != 0):
        print("{} to {} can be reached in {} steps.".format(beginWord, endWord, steps))
    else:
        print("{} to {} cannot be reached".format(beginWord, endWord))
