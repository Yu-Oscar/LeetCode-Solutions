function productExceptSelf(nums: number[]): number[] {
    let ans: number[] = []
    for (const num of nums) {
        ans.push(1)
    }

    let left: number = 1
    for (let i=0; i<nums.length; i++) {
        ans[i] = left
        left *= nums[i]
    }

    let right: number = 1
    for (let i=nums.length -1; i >= 0; i--) {
        ans[i] *= right
        right *= nums[i]
    }
    return ans
};