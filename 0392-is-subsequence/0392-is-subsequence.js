/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var isSubsequence = function(s, t) {
    t = t.split("");
    for (let i=0; i<s.length; i++) {
        if (t.indexOf(s.charAt(i)) === -1) return false
        else t.splice(0, t.indexOf(s.charAt(i))+1);    
    }
    return true
};
