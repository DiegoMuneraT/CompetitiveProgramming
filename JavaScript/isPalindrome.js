/**
 * @param {number} x
 * @return {boolean}
 */
var isPalindrome = function(x) {
  x = x.toString();
  const len = x.length;
  for(let i = 0; i < len / 2; i++){
    if(x[i] !== x[len - 1 - i]){
      return false
    }
  }
  return true
};
