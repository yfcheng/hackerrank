/**
 * @param {number[]} nums
 * @return {string}
 */

var greaterThan = function greaterThan(a, b){
	var aStr = a.toString(),
		bStr = b.toString();

	var first = aStr + '' + bStr,
		second = bStr + '' + aStr;

	if(parseInt(first) > parseInt(second)){
		return false;
	}
	else{
		return true;
	}
};

var largestNumber = function(nums) {
    var allZeros = true;
    for(var j = 0;j < nums.length;j++){
        if(nums[j] !== 0){
            allZeros = false;
            break;
        }
    }
    if(allZeros){
        return "0";
    }
    
	for(var i = 0; i < nums.length; i++){
		for(var j = 0;j < nums.length;j++){
			if(greaterThan(nums[j], nums[i])){
				var tmp = nums[j];
				nums[j] = nums[i];
				nums[i] = tmp;
			}
		}
	}
	var ans = nums.join('');
	return ans;
};


console.log( largestNumber([3, 30, 34, 5, 9]));
console.log( largestNumber([30, 3]));
console.log( largestNumber([824, 8247]));
console.log( largestNumber([98, 999]));
console.log( largestNumber([99998, 99]));
console.log( largestNumber([1, 20]));
console.log( largestNumber([20, 1]));
console.log( largestNumber([98,97,99]));
console.log( largestNumber([99,97,98]));
console.log( largestNumber([98,99,97]));
console.log( largestNumber([98, 999]) );
console.log( largestNumber([99998, 99]) );
console.log( largestNumber([55554, 55]) );
console.log( largestNumber([54, 5555]) );
console.log( largestNumber([55556, 55]) );
console.log( largestNumber([56, 5555]) );
