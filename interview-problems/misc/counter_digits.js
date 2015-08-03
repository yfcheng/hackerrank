/*Given a string having a pattern "11122333", or "1", return the strng containing the count of repeating characters and the digits i.e. "312233", "11"
*/

function compressStringPatterns(inputStr)
{    
    var inp = inputStr.trim().split(''),    //  .. convert string to an array
        prev='',
        count='',
        out='';

    for(var i = 0; i < inp.length; i++){
        if(prev === inp[i]){    //  .. if the prev character is same as the current one then increment the counter
            count = count + 1;
        }
        else{ 
            out = out + count + '' + prev;  //  .. else append the count of the character and the character 
            prev = inp[i];      //  .. reset the prev to the current one
            count = 1;          //  .. initialize the counter
        }
    }
    out = out + count + '' + prev;  // .. this is for appending the last count of the character and the character
    return out;
}

console.log( compressStringPatterns( '111223332' ));    //==> 31223312
console.log( compressStringPatterns( '1' ));            //==> 11
console.log( compressStringPatterns( '12' ));           //==> 1112
console.log( compressStringPatterns( '  ' ));           //==> ''
