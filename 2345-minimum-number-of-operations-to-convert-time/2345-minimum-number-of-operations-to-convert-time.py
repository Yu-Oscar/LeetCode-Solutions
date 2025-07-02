class Solution:
    def convertTime(self, current: str, correct: str) -> int:
        currHr = int(current[0:2])
        currMin = int(current[3:5])
        corrHr = int(correct[0:2])
        corrMin = int(correct[3:5])

        curr = currHr*60 + currMin
        corr = corrHr*60 + corrMin
        count = 0

        diff = corr-curr
        
        while diff > 0:
            if diff >= 60:
                diff -= 60 
            elif diff >= 15:
                diff -= 15
            elif diff >= 5:
                diff -= 5
            else:
                diff -= 1
            count += 1

        return count    
        
        