/**
 * @param {string[]} emails
 * @return {number}
 */
var numUniqueEmails = function(emails) {
    for (let i=0; i<emails.length; i++) {
        let atIndex = emails[i].indexOf('@');
        if (emails[i].indexOf('+') !== -1) {
            const plusIndex = emails[i].indexOf('+');
            emails[i] = emails[i].slice(0, plusIndex)
                                .replaceAll('.', '')
                                .concat(emails[i].slice(atIndex));
        } else emails[i] = emails[i].slice(0, atIndex)
                                  .replaceAll('.', '')
                                  .concat(emails[i].slice(atIndex));
    }
    return new Set(emails).size
};