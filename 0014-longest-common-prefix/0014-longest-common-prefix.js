/**
 * @param {string[]} strs
 * @return {string}
 */
var longestCommonPrefix = function(strs) {
    while (strs[0] !== "")
    {
        if (strs.filter(x => x.slice(0, strs[0].length).includes(strs[0])).length === strs.length) return strs[0];
        else (strs[0] = strs[0].slice(0, strs[0].length-1));
    }
    return ""
};