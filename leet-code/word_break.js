/**
  https://leetcode.com/problems/word-break-ii/
 * @param {string} s
 * @param {set<string>} wordDict
 * @return {string[]}
s = "catsanddog",
dict = ["cat", "cats", "and", "sand", "dog"].
A solution is ["cats and dog", "cat sand dog"].
*/

var permutation = function(s, dict, words, st, final){
  if(st >= s.length){
    return false;
  }
  var word =  '';
  for(var i = st; i < s.length; i++){
    word += s[i];
    if(dict[word]){
      words.push( word );
      if(!permutation(s, dict, words, i + 1, final)){
        var sent = '';
        for(var j = 0;j < words.length; j++){
          sent = sent + words[j] + ' ';
        }
        final.push( sent );
      }
      words = [];
    }
  }
  return final;
};

var wordBreak = function(s, wordDict) {
  var w = [],
      final = [];
  return permutation(s , dict, w, 0, final);
};


var s = 'catsanddog',
    dict = {'cat': true, 'cats': true, 'and': true, 'sand': true, 'dog': true };

console.log(  wordBreak(s, dict) );
