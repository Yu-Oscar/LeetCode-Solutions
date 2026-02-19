function containsDuplicate(nums: number[]): boolean {
    let set = new Set<number>()

    for (const num of nums) {
        if (set.has(num)) return true
        set.add(num)
    }
    console.log(set)
    return false
};