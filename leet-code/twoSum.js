// https://leetcode.com/problems/two-sum/

/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
  var out = [],
      temp = {};
      
  for(var i = 0;i < nums.length;i++){
      var num = nums[i],
      res = target - num;
      if(temp[num]){
          out.push( temp[num] );
          out.push( i + 1);
          break;
      }
      else{
          temp[res] = i + 1;
      }
  }
  return out;
};

console.log( twoSum([3,2,4],6));
