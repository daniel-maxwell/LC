/**
 * @param {string} s
 * @return {boolean}
 */
var isValid = function(s) {
    let stack = [];
    for (let i=0; i<s.length; i++) {
        switch (s.charAt(i)) {
            case "(":
                stack.push(0);
                break;

            case "{":
                stack.push(1);
                break;

            case "[":
                stack.push(2);
                break;

            case ")":
                if (stack.at(-1) === 0) stack.pop();
                else return false;
                break;
            
            case "}":
                if (stack.at(-1) === 1) stack.pop();
                else return false;
                break;

            case "]":
                if (stack.at(-1) === 2) stack.pop();
                else return false;
                break;

            default:
                return false;
        }
    }
    return stack.length === 0
};