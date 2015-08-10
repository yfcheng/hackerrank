#!/usr/local/bin/node

/*
SET a 10
SET b 10
NUMEQUALTO 10       2
NUMEQUALTO 20       0
SET b 30
NUMEQUALTO 10       1
END
*/

function SimpleDatabase()
{
  // .. private variables
  var reverseLookup = {},
    dataBag = {};

// .. private methods
var update = function (dict, key, incr){
      if(!dict[key]){
        dict[key] = incr;
      }
      else{
        dict[key] += incr;
      }
    },
    set = function(args){
      var key  = args[1],
          value = parseInt( args[2] );
      key = key.toString();
      update(dataBag, key, value);
      update(reverseLookup, value, 1);
    },
    numEqualTo = function(args){
      var key = args[1];
      key = key.toString();
      return (reverseLookup[key] ? reverseLookup[key] : '');
    },
    get = function(args){
      var key = args[1];
      key = key.toString();
      return dataBag[key];
    },
    unset = function(args){
      var key = args[1],
          val = dataBag[key];
      delete dataBag[key];
      reverseLookup[val] -= 1;
    };


  // .. public methods
  this.processCommand = function(cmd){
    var args = cmd.split('\n'),
        args = args[0].split(' ');
    // if(args && Array.isArray(args) && args.length > 0){} // .. do validation of the input args
    switch(args[0]){
      case 'SET':
        return set(args);
      case 'NUMEQUALTO':
        return numEqualTo(args);
      case 'UNSET':
        return unset(args);
      case 'GET':
        return get(args);
      case 'END':
        dataBag = {};
        reverseLookup = {};
      break;
    }
  };
}


module.exports = SimpleDatabase;
