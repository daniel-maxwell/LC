from sortedcontainers import SortedList
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mapping = {}
        for i in range(0, len(strs)):
            hashWord = SortedList([])
            for letter in strs[i]:
                hashWord.add(ord(letter))
            hashWord = repr(hashWord)
            if hashWord in mapping:
                mapping[hashWord].append(strs[i])
            else:
                mapping[hashWord] = [strs[i]]
        return mapping.values()