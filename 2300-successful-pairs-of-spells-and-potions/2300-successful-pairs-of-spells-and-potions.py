class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        pairs = []
        potions.sort()

        def getNumSuccessfulPairs(spell):
            l, r = 0, len(potions) - 1

            if spell * potions[l] >= success:
                return len(potions)

            while l <= r:
                m = l + ((r-l)//2)

                if spell * potions[m] < success:
                    l = m + 1
                else:
                    r = m - 1

            return (len(potions) - 1) - r
   
        for spell in spells:
            pairs.append(getNumSuccessfulPairs(spell))
            
        return pairs