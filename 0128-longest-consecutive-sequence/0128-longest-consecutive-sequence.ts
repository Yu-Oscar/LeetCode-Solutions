function longestConsecutive(nums: number[]): number {
    const set = new Set(nums)
    let longest = 0

    for (const num of set) {
        if (!set.has(num-1)) {
            let curr = 1
            while (set.has(num+curr)) {
                curr++
            }
            longest = Math.max(curr, longest)
        }
    }
    return longest
}