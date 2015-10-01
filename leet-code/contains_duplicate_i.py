"""
https://leetcode.com/problems/contains-duplicate/

Given an array of integers, find if the array contains any duplicates. Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.
"""

var containsDuplicate = function(nums)
{
    var dict = {};
    for(var i = 0;i < nums.length;i++){
        if(dict[nums[i]]){
            return false;
        }
        dict[ nums[i] ] = true;
    }
    return true;
};


console.log( containsDuplicate([]) );
console.log( containsDuplicate([1]) );
console.log( containsDuplicate([1,3,1]) );
console.log( containsDuplicate([1,2,3]) );
