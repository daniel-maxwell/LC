/**
 * @param {string} pattern
 * @param {string} s
 * @return {boolean}
 */
var wordPattern = function(pattern, s) {
    s = s.split(" ");
    if (new Set(pattern.split("")).size !== new Set(s).size) return false;
    let map = {};
    for (let i=0; i<s.length; i++)
    {
        if (pattern.charAt(i) in map && map[pattern.charAt(i)] !== s[i]) return false;
        map[pattern.charAt(i)] = s[i];
    } 
    const values = Object.values(map);
    return new Set(s).size === Object.values(map).length;
};