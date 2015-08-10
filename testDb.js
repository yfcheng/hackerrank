var _db = require('./SimpleDatabase'),
    db = new _db();

var cmds = [
  'SET A 10',
  'SET B 10',
  'SET C 20',
  'NUMEQUALTO 20',
  'NUMEQUALTO 10',
  'UNSET A',
  'GET A',
  'NUMEQUALTO 10'
];

var that = this;
cmds.forEach(function(cmd){
  that.db.processCommand

});
