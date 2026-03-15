function subsets(nums: number[]): number[][] {
    let ans = []

    function recurr(cans, curr) {
        ans.push([...curr])

        for (let i = 0; i < cans.length; i++) {
            curr.push(cans[i]);
            recurr(cans.slice(i + 1), curr);
            curr.pop();
        }
        
    }
    recurr(nums,[])
    return ans
};