function findMin(nums: number[]): number {
    let left = 0 
    let right = nums.length -1 

    if (nums[left] < nums[right]) return nums[left]

    while (right-left > 1) {
        let mid = Math.floor((left + right) / 2)

        if (nums[mid] > nums[left]) {
            left = mid
        } else {
            right = mid
        }
    }
    return nums[right]
};