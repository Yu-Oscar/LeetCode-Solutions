function dailyTemperatures(temperatures: number[]): number[] {
    let stack = []
    const ans = new Array(temperatures.length).fill(0);

    for (let i = 0; i < temperatures.length; i++) {
        while (temperatures[i] > temperatures[stack[stack.length-1]] && stack.length) {
            const j = stack.pop()
            ans[j] = i - j
        }
        stack.push(i)
    }
    return ans
};