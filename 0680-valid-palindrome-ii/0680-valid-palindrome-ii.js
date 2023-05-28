/**
 * @param {string} s
 * @return {boolean}
 */
var validPalindrome = function(s) {
    if (s.length < 3) return true;
    if (s.length < 4 && s[0] !== s[s.length-1]) return false;
    let i = 0, j = s.length -1;
    while (j-i > s.length % 2 +1) {
        if (s.charAt(i) !== s.charAt(j)) {
            const w = s.slice(i+1, j);
            const x = s.split("").reverse().slice(i+2, j+1).join("");
            const y = s.slice(i+2, j+1);
            const z = s.split("").reverse().slice(i+1, j).join("");
            return w === x || y === z ? true : false;
        }
        i++, j--; 
    }
    return true
};