/**
 * @param {number[]} arr
 * @return {number[]}
 */
var replaceElements = function(arr) {
    for (let i=0; i<arr.length-1; i++) {
        let greatestEl = arr[i+1];
        for (let j=i+1; j<arr.length; j++) {
            if (arr[j] > greatestEl) greatestEl = arr[j];
        }
        arr[i] = greatestEl;
    }
    arr[arr.length-1] = -1;
    return arr
};