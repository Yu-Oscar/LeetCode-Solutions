function subsetsWithDup(nums: number[]): number[][] {
    nums = nums.sort()
    let ans = []

    function recurr(idx, curr) {
        ans.push([...curr])

        for (let i = idx; i < nums.length; i++) {
            curr.push(nums[i]);
            recurr(i + 1, curr);
            let temp = curr.pop();
            while (i+1 < nums.length && temp == nums[i+1]) i ++
        }
        
    }
    recurr(0,[])
    return ans
};