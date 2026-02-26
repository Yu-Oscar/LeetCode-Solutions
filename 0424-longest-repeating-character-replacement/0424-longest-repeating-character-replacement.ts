function characterReplacement(s: string, k: number): number {
    const freq = []
    let ans = 0
    let max = 0
    let l = 0

    for (let r = 0; r < s.length; r++) {
        freq[s[r]] = (freq[s[r]] || 0) + 1
        max = Math.max(max, freq[s[r]])

        if ((r-l+1-max) > k) {
            freq[s[l]]--
            l++
        }
        ans = Math.max(ans, r - l + 1)
    }

    return ans
};