function groupAnagrams(strs: string[]): string[][] {
    let map = new Map<string, string[]>();

    for (const str of strs) {
        let sorted = str.split('').sort().join('')

        if (!map.has(sorted)) {
            map.set(sorted, [])
        }
        map.get(sorted).push(str);
    }
    return [...map.values()]
};