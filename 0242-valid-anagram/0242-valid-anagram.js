/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var isAnagram = function(s, t) {
    if (s.length != t.length) return false


    for (let i=0; i < s.length; i++)
    {
        if (t.includes(s[i])) {
            t = t.slice(0, t.indexOf(s[i])) + t.slice(t.indexOf(s[i])+1)
        }
        else return false
    }
    return true
};