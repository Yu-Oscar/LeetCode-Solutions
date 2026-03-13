function search(nums: number[], target: number): number {
    let left = 0 
    let right = nums.length -1 

    while (left < right) {
        let mid = Math.floor((left + right) / 2)
        console.log(left,right,mid)

        if (nums[mid] == target) return mid

        if (nums[left] < nums[mid]) {
            if (target == nums[left]) return left
            if (nums[left] < target && target < nums[mid]) {
                right = mid - 1
            } else {
                left = mid + 1
            }
        } else {
            if (target == nums[right]) return right
            if (nums[mid] < target && target < nums[right]) {
                left = mid + 1
            } else {
                right = mid - 1
            }
        }
        console.log(left,right,mid)
    }
    
    return nums[left] == target ? left : -1
};