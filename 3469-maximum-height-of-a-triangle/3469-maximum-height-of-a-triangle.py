class Solution:
    def maxHeightOfTriangle(self, red: int, blue: int) -> int:
        def start(start_red: bool) -> int:
            r, b = red, blue
            h = 0
            isRed = start_red
            
            while True:
                addh = h + 1

                if isRed:
                    if r >= addh:
                        r -= addh
                        h = addh
                        isRed = False
                    else:
                        break
                else: 
                    if b >= addh:
                        b -= addh
                        h = addh
                        isRed = True
                    else:
                        break
            
            return h

        return max(start(True), start(False))

        

        