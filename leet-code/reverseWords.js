/**
 * @param {string} str
 * @returns {string}
 */
var reverseWords = function(str) {
    if(!str){
        return "";
    }
    var out = "",
        temp = "";
    for(var i = 0;i < str.length;i++){
     if( str[i] === " "){
         out = (temp.trim().length !== 0) ? temp + " " + out : out;
         temp = "";
     }
     else {
         temp += str[i];
     }
    }
    var hasChar = false;
    for(var i = 0; i < temp.length; i++){
        if(temp[i] !== " "){
            hasChar = true;
            break;
        }
    }
    if(hasChar){
       out = temp + " " + out; 
    }
    return out.trim();
};
console.log( reverseWords(" "), "|");
console.log( reverseWords("the sky is blue"), "|");
console.log( reverseWords("  a  b "), "|");
//console.log( reverseWords(" 1  "), "|");