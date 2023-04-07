/**
* @param {number[]} nums
* @return {number[]}
* [n, n+n+1, n+1+n+2, n+2+n+3]
*/
var runningSum = function(nums){
    for (let i = 0; i < nums.length - 1; i++){
      let temp = nums[i] + nums[i+1]
      nums[i+1] = temp
    }
    return nums
  };
  
  const numsArray = [1,2,3,4]
  console.log(runningSum(numsArray))
  