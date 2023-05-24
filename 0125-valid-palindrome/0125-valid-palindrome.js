/**
 * @param {string} s
 * @return {boolean}
 */
var isPalindrome = function(s) {
    s = s.replace(/[^A-Za-z0-9]/g, '').toLowerCase().split("");
    return s.toString() === s.reverse().toString() ? true : false;
};
