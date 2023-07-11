/**
 * @param {Array} arr
 * @param {number} size
 * @return {Array[]}
 */
var chunk = function(arr, size) {
    let output = [];
    let i = 0;
    while (i < arr.length) {  
        if (arr.length - i < size) {
            output.push(arr.slice(i));
            return output;
        }
        let chunk = [];
        let j = i;
        while (j - i < size && j < arr.length) {
            chunk.push(arr[j]);
            j++;
        }
        output.push(chunk)
        i = j;
    };
    return output;
};
