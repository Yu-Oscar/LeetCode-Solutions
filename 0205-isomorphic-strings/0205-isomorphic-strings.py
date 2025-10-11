class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        smap, tmap = {}, {}

        for schar, tchar in zip(s,t):
            if schar in smap and smap[schar] != tchar:
                return False
            if tchar in tmap and tmap[tchar] != schar:
                return False

            smap[schar] = tchar
            tmap[tchar] = schar

        return True

            