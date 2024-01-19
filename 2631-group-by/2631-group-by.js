/**
 * @param {Function} fn
 * @return {Object}
 */
Array.prototype.groupBy = function(fn) {
    let output = {};
    for (let i=0; i<this.length; i++){
        const key = fn(this[i])
        if (output[key] == undefined) {
            output[key] = [this[i]];
        } 
        else {
            output[key].push(this[i]);
        }
    }
    return output;
};

/**
 * [1,2,3].groupBy(String) // {"1":[1],"2":[2],"3":[3]}
 */