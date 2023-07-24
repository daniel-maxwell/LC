class Solution:
    def addBinary(self, a: str, b: str) -> str:
        output, i, carryBit = "", 1, 0

        while i <= len(a) and i <= len(b):

            if int(a[-i]) + int(b[-i]) == 2:

                if carryBit == 1: output = "1" + output
                else:
                    carryBit = 1
                    output = "0" + output

            elif int(a[-i]) + int(b[-i]) == 1:

                if carryBit == 1: output = "0" + output
                else: output = "1" + output
            
            else:
                if carryBit == 1:
                    carryBit -= 1
                    output = "1" + output
                else: output = "0" + output

            i += 1

        
        if len(a) != len(b):
            excess = a[:len(a) - len(b)] if len(a) > len(b) else b[:len(b) - len(a)]
            if carryBit > 0:
                for i in range(len(excess) -1, -1, -1):
                    if int(excess[i]) + carryBit == 2:
                        excess = excess[:i] + "0" + excess[i+1:]

                    else:
                        carryBit -= 1
                        excess = excess[:i] + "1" + excess[i+1:]
                        break
 
                if carryBit == 1:
                    carryBit -= 1  
                    excess = "1" + excess
                output = excess + output

            else: output = excess + output

        if carryBit > 0: return str(carryBit) + output

        else: return output