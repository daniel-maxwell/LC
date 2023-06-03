/**
 * @param {number} numRows
 * @return {number[][]}
 */
var generate = function(numRows) {
    let output = [];
    for (let i=0; i<numRows; i++) {
        const rowSize = i+1;
        let row = [];
        for (let j=0; j<rowSize; j++) {
            j === 0 || j === rowSize-1 ? row.push(1): row.push(output[i-1][j-1] + output[i-1][j]);
        }
        output.push(row);
    }
    return output
};