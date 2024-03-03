class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        charCounts, res = {}, []
        wordCounts = {}

        for word in strs:
            if word in wordCounts:
                wordCounts[word] += 1
            else:
                wordCounts[word] = 1

            charCounts[word] = {}
            for char in word:
                if char in charCounts[word]:
                    charCounts[word][char] += 1
                else:
                    charCounts[word][char] = 1

        while charCounts:
            currWord = strs.pop()
            if currWord not in charCounts:
                continue
            currDict = charCounts.pop(currWord)
            group = [currWord] * wordCounts[currWord]
            groupSize = len(group)

            for word, charCount in charCounts.items():
                if currDict == charCount:
                    group.append(word)

            if len(group) > groupSize:
                for i in range(groupSize, len(group)):
                    charCounts.pop(group[i])

            res.append(group)

        return res