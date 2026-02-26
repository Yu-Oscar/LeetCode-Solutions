function maxProfit(prices: number[]): number {
    let max = -Infinity
    let min = Infinity;

    for (const price of prices) {
        min = Math.min(min, price)
        max = Math.max(max, price-min)
        
    }
    return max
};