function isAnagram(s: string, t: string): boolean {
    if (s.length !== t.length) return false;
    
    const counter = {}

    for (const char of s) {
        counter[char] = (counter[char] || 0) + 1
    }

    for (const char of t) {
        if (!counter[char]) return false
        counter[char] -= 1
        if (counter[char] < 0) return false
    }
    return true
};