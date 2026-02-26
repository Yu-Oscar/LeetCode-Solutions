function maxArea(height: number[]): number {
    let l = 0;
    let r = height.length-1; 
    let max = 0 
    while (l < r) {
        let curr = (r - l) * Math.min(height[l], height[r])
        max = Math.max(max, curr)

        if (height[l] < height[r]) {
            l++;
        } else {
            r--;
        }
    }
    return max
};