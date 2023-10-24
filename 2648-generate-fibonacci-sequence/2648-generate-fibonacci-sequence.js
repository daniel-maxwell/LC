/**
 * @return {Generator<number>}
 */
var fibGenerator = function*() {
    let fibs = [0, 1];
    yield 0;
    yield 1;
    
    while (true) {
        fibs.push(fibs[fibs.length - 2] + fibs[fibs.length - 1])
        yield fibs[fibs.length - 1]
    }
};

/**
 * const gen = fibGenerator();
 * gen.next().value; // 0
 * gen.next().value; // 1
 */