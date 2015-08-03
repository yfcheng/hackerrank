
//https://leetcode.com/problems/implement-strstr/

/**
 * @param {string} haystack
 * @param {string} needle
 * @return {number}
 */

 var isAllCharsFound = function(hayStack, needle, st){
     var isFound = true,
         j = 0;

     while(j < needle.length){
         if(hayStack[st] !== needle[j]){
             isFound = false;
             break;
         }
         else{
             st += 1;
             j += 1;
         }
     }
     return isFound;
 };
 var strStr = function(haystack, needle) {
    if(!needle && !haystack){
        return 0;
    }
    if(!haystack && needle){
        return -1;
    }
    if(haystack && !needle){
        return 0;
    }
    if(needle.length > haystack.length){
        return -1;
    }
    var hId = 0,
        isFound = false;  //haystack idx
    while((hId + needle.length) <= haystack.length){
        if(haystack[hId] === needle[0]){
            if(isAllCharsFound(haystack, needle, hId)){
                isFound = true;
                break;
            }
        }
        hId += 1;
    }
    return isFound ? hId : -1;
};