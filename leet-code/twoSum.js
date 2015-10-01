/**
https://leetcode.com/problems/two-sum/

Given an array of integers, find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2. Please note that your returned answers (both index1 and index2) are not zero-based.

You may assume that each input would have exactly one solution.

Input: numbers={2, 7, 11, 15}, target=9
Output: index1=1, index2=2
**/

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
