/**
 * @param {integer} init
 * @return { increment: Function, decrement: Function, reset: Function }
 */
var createCounter = function(init) {
    counter = new Object(init);
    counter.original = init,
    counter.init = init,

    counter.increment = function() {
        ++this.init;
        return this.init;
    },
    counter.decrement = function(){
        --this.init;
        return this.init;
    },
    counter.reset = function() {
        this.init = this.original;
        return this.init;
    }
    return counter;
};

/**
 * const counter = createCounter(5)
 * counter.increment(); // 6
 * counter.reset(); // 5
 * counter.decrement(); // 4
 */