/**
 * @param {number} n
 * @return {boolean}
 */ 
var isHappy = function(n) {
	if(n === 1){
		return true;
	}
	var container = {};

	while(true){
		sum = 0;
		while(n > 0){
			var digit = n % 10;
			sum += digit * digit;
			n = (n - digit) / 10;
		}
		n = sum;
		if(n === 1){
			return true;
		}
		if(n === 4){
			return false;
		}
		var sorted = parseInt( sum.toString().split('').sort().join(''));
		if(sorted === 4 || sorted === 16 || sorted === 37 || sorted === 58 || sorted === 89 || sorted === 145 || sorted === 24 || sorted === 2){
			return false;
		}
		if(container[sorted] === true){
			return false;
		}
		container[sorted] = true;
	}
	return false;
};

//console.log( isHappy(7));
console.log( isHappy(10598542));