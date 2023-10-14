class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        hashWords, charMap = [], {}

        for i in range(0, len(order)):
            charMap[order[i]] = i+1

        for w in range(0, len(words)):
            word, l, temp = words[w], 0, []

            while l < len(word):
                hashedLetter = charMap[word[l]]
                temp.append(hashedLetter)
                l += 1
            hashWords.append(temp)

        i, j = 1, 0
        
        while i < len(hashWords):
            wordA, wordB = hashWords[i-1], hashWords[i]
            equal = True

            while j < len(wordA) and j < len(wordB):
                if wordA[j] < wordB[j]:
                    equal = False
                    break
                elif wordA[j] > wordB[j]:
                    return False
                j += 1
            
            if equal and len(wordA) > len(wordB):
                return False
            i += 1

        return True