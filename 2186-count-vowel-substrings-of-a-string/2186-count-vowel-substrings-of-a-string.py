class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        s = set("aeiou")
        n = len(word)
        ans = 0
        
        for i in range(n):
            if word[i] not in s:
                continue

            seen = set()
            for j in range(i, n):
                if word[j] not in s:
                    break
                seen.add(word[j])
                if len(seen) == 5: 
                    ans += 1

        return ans