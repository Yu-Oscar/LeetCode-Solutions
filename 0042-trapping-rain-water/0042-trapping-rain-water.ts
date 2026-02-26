function trap(height: number[]): number {
    const rightMax = new Array(height.length);
    rightMax[height.length - 1] = height[height.length - 1];

    for (let i = height.length - 2; i >= 0; i--) {
        rightMax[i] = Math.max(rightMax[i + 1], height[i]);
    }
    const leftMax = [height[0]]
    let ans = 0
    for (let i = 1; i < height.length; i++) {
        let curr = height[i]
        leftMax.push(Math.max(leftMax[i-1], curr))
        ans += (Math.min(leftMax[i], rightMax[i]) - curr)
    }
    return ans
};