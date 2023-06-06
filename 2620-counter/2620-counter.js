/**
 * @param {number} n
 * @return {Function} counter
 */
let calls = 0;
var createCounter = function(n) {
    let calls = -1;
    return function() {
            calls++;
            return n + calls
        } 
};

/** 
 * const counter = createCounter(10)
 * counter() // 10
 * counter() // 11
 * counter() // 12
 */