/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var isIsomorphic = function(s, t) {
    let hmap1 = {},
        hmap2 = {};
    for (let i=0; i<s.length; i++) {
        hmap1[`#${s.charAt(i)}`] = i;
        hmap2[`#${t.charAt(i)}`] = i;
    }
    return Object.values(hmap1).toString() === Object.values(hmap2).toString() ? true : false;
};