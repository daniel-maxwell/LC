class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        substrMatch = False
        short = str1 if len(str1) <= len(str2) else str2
        long = str2 if len(str1) <= len(str2) else str1
        originalShort = short

        while not substrMatch:

            if short == "": substrMatch = True 
        
            elif (short == long[:len(short)] and len(long) % len(short) + 
                                                (len(str1) % len(short)) +
                                                (len(str2) % len(short)) == 0):
                substrMatch = True
                for i in range(0, len(originalShort), len(short)):
                    if short != originalShort[i:i+len(short)]:
                        substrMatch = False
                        short = short[:-1]
                        break
                if substrMatch:
                    for i in range(0, len(long), len(short)):
                        if short != long[i:i+len(short)]:
                            substrMatch = False
                            short = short[:-1]
                            break

            else:
                short = short[:-1]

        return short