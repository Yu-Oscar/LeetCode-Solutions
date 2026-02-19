function isAnagram(s: string, t: string): boolean {
    if (s.length !== t.length) return false;
    let dict: { [key: string]: number } = {};

    for (const char of s) {
        dict[char] = (dict[char] || 0) + 1;
    }

    for (const char of t) {
        if (!dict[char]) return false;

        dict[char] -= 1;
        if (dict[char] < 0) return false;
    }
    return true
};