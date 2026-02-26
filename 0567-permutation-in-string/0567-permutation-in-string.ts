function checkInclusion(s1: string, s2: string): boolean {
    if (s1.length > s2.length) return false;

    let freq1 = new Array(26).fill(0);
    let freq2 = new Array(26).fill(0);

    for (let i = 0; i < s1.length; i++) {
        freq1[s1.charCodeAt(i) - 97]++;
        freq2[s2.charCodeAt(i) - 97]++;
    }

    let l = 0;
    let match = 0;

    for (let i = 0; i < 26; i++) {
        if (freq1[i] == freq2[i]) match++;
    }

    for (let r = s1.length; r < s2.length; r++) {
        if (match == 26) return true;

        let idx = s2.charCodeAt(l) - 97;
        if (freq1[idx] == freq2[idx]) match--;
        freq2[idx]--;
        if (freq1[idx] == freq2[idx]) match++;

        idx = s2.charCodeAt(r) - 97;
        if (freq1[idx] == freq2[idx]) match--;
        freq2[idx]++;
        if (freq1[idx] == freq2[idx]) match++;

        l++;
    }

    return match == 26;
}