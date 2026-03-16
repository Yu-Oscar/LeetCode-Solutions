function combinationSum(candidates: number[], target: number): number[][] {
    let ans = []
    function recurr(idx, can, sum) {
        for (let i = idx; i < candidates.length; i++ ) {
            let curr = candidates[i]
            console.log(idx, can, sum, curr)
            if (sum + curr < target) {
                can.push(curr)
                sum += curr
                recurr(i, can, sum)
                can.pop()
                sum -= curr
            } else if (sum + curr == target) {
                
                can.push(curr)
                ans.push([...can])
                can.pop()
            }
        }
    }

    recurr(0,[], 0)
    return ans

};