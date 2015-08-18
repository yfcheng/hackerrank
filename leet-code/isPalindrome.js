/**
 * @param {string} s
 * @return {boolean}
 */

var isAlphaNumeric = function(a)
{
    var code = a.charCodeAt();
    // .. number
    return ((code > 47 && code < 58) ||
            (code > 96 && code < 123) ||
            (code > 64 && code < 91))
};
var isPalindrome = function(s) {
    if(s.trim().length === 0){
        return true;
    }
    var st = 0,
        end = s.length - 1;
    var isPalindrome = true;
    while(st < end){
        if(!isAlphaNumeric(s[st])){
            st += 1;
            continue;
        }
        if(!isAlphaNumeric(s[end])){
            end -= 1;
            continue;
        }
        if(s[st].toUpperCase() !== s[end].toUpperCase()){
            isPalindrome = false;
            break;
        }
        st += 1;
        end -= 1;
    }
    return isPalindrome;
};
