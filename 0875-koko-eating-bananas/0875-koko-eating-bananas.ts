function minEatingSpeed(piles: number[], h: number): number {
    let ceil = Math.max(...piles)

    let left = 1
    let right = ceil
    while (left <= right) {
        let rate = Math.floor((left+right)/2)

        let total = 0
        for (const pile of piles) {
            total += Math.ceil(pile/rate)
        }
        if (total > h) { //eat too slow 
            left = rate + 1 //eat faster 
        } else {
            right = rate //finish
        }
        if (left == right) return right
    }
    return 0
};