function threeSum(nums: number[]): number[][] {
    nums = nums.sort((a,b) => a-b);
    let ans= []

    for (let i = 0; i < nums.length - 2; i++) {
        if (nums[i] === nums[i - 1]) continue;

        let curr = nums[i]
        let l = i+1;
        let r = nums.length-1
        while (l<r) {
            let sum = curr + nums[l] + nums[r]
            if (sum == 0) {
                ans.push([curr, nums[l], nums[r]])

                while (nums[l] === nums[l+1]) l++;
                while (nums[r] === nums[r-1]) r--;
            }

            if (sum > 0) {
                r--;
            } else {
                l++;
            }
        }
    }

    return ans
};