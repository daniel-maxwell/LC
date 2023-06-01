/**
 * @param {number[]} flowerbed
 * @param {number} n
 * @return {boolean}
 */
var canPlaceFlowers = function(flowerbed, n) {
    if (n === 0) return true;
    if (flowerbed.length === 1) return flowerbed[0] === 0;
    if (flowerbed.length === 2) return flowerbed[0] === 0 && flowerbed[1] === 0 && n < 2;
    
    let availablePlaces = 0;
    
    for (let i=0; i<flowerbed.length; i++) {
        if (i===0) {
            if (flowerbed[i] === 0 && flowerbed[i+1] === 0) {
                availablePlaces+=1;
                i+=1;
            }
        }
        else if (i === flowerbed.length-1) {
            if (flowerbed[i-1] === 0 && flowerbed[i] === 0) {
                availablePlaces+=1;
                i+=1;
            }
        } else {
            if (flowerbed[i-1] === 0 && flowerbed[i] === 0 && flowerbed[i+1] === 0) {
                availablePlaces+=1;
                i+=1;
            }
        }
    }
    return n <= availablePlaces
};