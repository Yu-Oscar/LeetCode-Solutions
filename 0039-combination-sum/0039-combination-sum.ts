function combinationSum(candidates: number[], target: number): number[][] {
    let ans = []
    candidates.sort((a,b) => a - b)

    function recurr(idx, can, sum) {
        for (let i = idx; i < candidates.length; i++ ) {
            let curr = candidates[i]
            if (sum + curr < target) {
                can.push(curr)
                sum += curr
                recurr(i, can, sum)
                can.pop()
                sum -= curr
                while (i+1 < candidates.length && curr == candidates[i+1]) i ++
            } else if (sum + curr == target) {
                can.push(curr)
                ans.push([...can])
                can.pop()
                break
            } else break
        }
    }

    recurr(0,[], 0)
    return ans

};