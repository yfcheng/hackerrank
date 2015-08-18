/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var isAnagram = function(s, t) {
    if(s === t){
        return true;
    }
    var dict = {};
    for(var i = 0;i < s.length; i++){
        var alpha = s[i],
            cnt = 1;
        dict[alpha] = (dict[alpha] ? (dict[alpha] + 1) : 1);
    }

    var isAnagram = true;
    for(var j = 0;j < t.length; j++){
        var curr = t[j];
        if(!dict[curr]){
            isAnagram = false;
            break;
        }
        else{
            if(dict[curr] === 1){
                delete dict[curr];
            }
            else{
                var cnt = dict[curr];
                dict[curr] = cnt - 1;
            }
        }
    }
    if(isAnagram && dict && Object.keys(dict).length > 0){
        isAnagram = false;
    }
    return isAnagram;
};
