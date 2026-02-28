function longestConsecutive(nums: number[]): number {
    let set = new Set(nums)
    let ans = 0

    for (const num of set) {
        let len = 1
        if (!set.has(num-1)) {
            while (set.has(num+len)) {
                len++
            }
            ans = Math.max(ans, len)
        }
    }
    return ans
};