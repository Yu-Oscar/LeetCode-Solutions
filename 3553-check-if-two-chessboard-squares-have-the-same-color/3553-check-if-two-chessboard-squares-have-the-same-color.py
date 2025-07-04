class Solution:
    def checkTwoChessboards(self, coordinate1: str, coordinate2: str) -> bool:
        
        def checkblack(coor):
            if ord(coor[0]) % 2 == 0:
                if int(coor[1]) % 2 == 0:
                    return True
                else:
                    return False
            else:
                if int(coor[1]) % 2 == 0:
                    return False
                else:
                    return True

        return checkblack(coordinate1) == checkblack(coordinate2) 
        