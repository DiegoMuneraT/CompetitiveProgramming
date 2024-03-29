/**
* @param {number[]} nums
* @param {number} target
* @return {number[]}
*/
var twoSum = function(nums, target){
    let hash = {}
    
    for (let i = 0; i < nums.length; i++){
      const n = nums[i];
      if (hash[target - n] !== undefined){
        return [hash[target - n], i];
      }
      hash[n] = i;
    }
    return [];
  }
  
  let nums = [2,7,11,15]
  let target = 9
  console.log(twoSum(nums, target))