/**
 * @param {string} digits
 * @return {string[]}
 */

 var letterCombinations = function(digits) {
     if(!digits){
         return [];
     }
     var dict = {'2':['a','b','c'],'3':['d','e','f'],'4':['g','h','i'],'5':['j','k','l'],'6':['m','n','o'],'7':['p','q','r','s'],'8':['t','u','v'],'9':['w','x','y','z']};
     var out = dict[ digits[0] ];
     for(var i = 1; i < digits.length; i++){
         var keycodeMap = dict[ digits[i] ];
         var temp = [];
         for(var j = 0;j < out.length;j++){
             for(var k = 0; k < keycodeMap.length; k++){
                 temp.push( out[j] + '' + keycodeMap[k] );
             }
         }
         out = temp;
     }
     return out;
 };

console.log( letterCombinations('120') );
