/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLastWord = function(s) {
  var spaceIndex;
  for (var i=0; i<s.length-1; i++)
    {
      if (s.charAt(i) === " " && 
          !(s.charAt(i+1) === "" || 
            s.charAt(i+1) === " " ))
      {
        spaceIndex = i+1;
      }
    }
  var finalword = s.slice(spaceIndex);

  while (finalword[finalword.length-1] === " ")
  {
    finalword = finalword.slice(0, finalword.length -1);
  }
  return finalword.length
};