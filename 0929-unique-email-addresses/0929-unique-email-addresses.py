class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        emailSet = set()
        for i in range(0, len(emails)):
            plusFlag = False
            j=0

            while j < len(emails[i]):
                if emails[i][j] == '@': 
                    emailSet.add(emails[i])
                    break
                    
                if emails[i][j] == '+': plusFlag = True
                if plusFlag == True:
                    emails[i] = emails[i][:j] + emails[i][(j+1):]
                    j-=1

                if emails[i][j] == '.': 
                    emails[i] = emails[i][:j] + emails[i][(j+1):]
                    j-=1

                j+=1

        return len(emailSet)