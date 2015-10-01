/*Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.
For example,
"A man, a plan, a canal: Panama" is a palindrome.
"race a car" is not a palindrome.
Note:
Have you consider that the string might be empty? This is a good question to ask during an interview.
For the purpose of this problem, we define empty string as valid palindrome.
*/

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
