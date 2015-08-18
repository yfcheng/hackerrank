/*
Given a column title as appear in an Excel sheet, return its corresponding column number.
For example:
    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28
    AZ -> 52
    ELJ -> 3702
*/


/**
 * @param {string} s
 * @return {number}
 */
var titleToNumber = function(s) {
    var dict = {"A":1,"B":2,"C":3,"D":4,"E":5,"F":6,"G":7,"H":8,"I":9,"J":10,"K":11,"L":12,"M":13,"N":14,"O":15,"P":16,"Q":17,"R":18,"S":19,"T":20,"U":21,"V":22,"W":23,"X":24,"Y":25,"Z":26}

    var res = 0,
        idx = 0;
    for(var i = s.length - 1; i >= 0; i-- ){
        var curr = Math.pow(26, idx);
        curr *= dict[ s[i] ];
        res += curr;
        idx++;
    }
    return res;
};

console.log( titleToNumber('AA') );
console.log( titleToNumber('AZ') );
console.log( titleToNumber('AB') );
console.log( titleToNumber('ELJ') );
