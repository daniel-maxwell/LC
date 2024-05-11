class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        sequences, res = {}, []
        l, r = 0, 9
        while r < len(s):
            sequence = s[l:r+1]
            if sequence in sequences:
                if sequences[sequence] == 1:
                    res.append(sequence)
                    sequences[sequence] += 1
            else:
                sequences[sequence] = 1
            l += 1
            r += 1

        return res