/**
 * @param {number[]} nums
 * @return {boolean}
 */
const containsDuplicate = (nums) => {
  let hash = {}
  
  for(let i = 0; i < nums.length; i++){
    const n = nums[i];
    if(hash[n] !== undefined){
      return true;
    }
    hash[n] = i;
  }
  return false;
}

