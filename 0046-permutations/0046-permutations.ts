function permute(nums: number[]): number[][] {
    let ans = []

    function recurr(nums, curr) {
        if (nums.length == 0) {
            ans.push([...curr])
            return 
        }
        for (let i = 0; i < nums.length; i++) {
            let [removed] = nums.splice(i, 1)
            curr.push(removed)
            recurr(nums, curr)
            curr.pop()
            nums.splice(i, 0, removed)
        }
    }

    recurr(nums, [])
    return ans
};