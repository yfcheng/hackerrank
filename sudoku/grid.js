var fs = require('fs'),
	data = fs.readFileSync('qs.txt','utf-8'),
	split = data.split(''),
	grid = [],
	row = [];
for(var i = 0;i < split.length; i++){
	if(i !== 0 && (i + 1) % 9 === 1){
		grid.push( row );
		row = [];
	}
	var cell = split[i] === '.' ? 0 : parseInt( split[i] );
	row.push( cell );
}
grid.push( row );

function Set(){
	var items = {},
		_coll = [];
	this.Add = function Add(item){
		if(!items[item]){
			_coll.push( item );
			items[item] = _coll.length - 1;
		}
	};

	this.Remove = function Remove(item){
		if(items[item]){
			var id = items[item];
			_coll.splice( id, 1);
			delete items[item];
		}
	};

	this.Length = function Length(){
		return _items.length;
	};

	this.Items = function Items(){
		return _coll;
	};
};


var possible = function possible(grid, r, c){
	var bool = {};
	var _set = new Set();
	for(var i = 1;i <= 9;i++){
		_set.Add( i );
	}

	var val = 0;
	// check all possible values in row
	for(var i = 0; i < grid.length;i++){
		val = grid[i][c];
		if(val !== 0){
			_set.Remove( val );
		}
	}

	// check all possible values in col
	for(var i = 0;i < grid[0].length;i++){
		val = grid[r][i];
		if( val !== 0){
			_set.Remove( val );
		}
	}

	// check all possible in grid
	var x = r <= 2 ? 0: (r <= 5 ? 3 : 6),
		y = c <= 2 ? 0: (c <= 5 ? 3 : 6);

	for(var i = x; i < (x + 3); i++){
		for(var j = y; j< (y + 3); j++){
			val = grid[i][j];
			if(val !== 0){
				_set.Remove( val );
			}
		}
	}
	return _set.Items();
};


var point = {};
var solve = function solve(grid){

	var minx,miny,minpossible = 9;
	for(var i = 0;i < grid.length;i++){
		for(var j = 0;j < grid[0].length;j++){
			if(grid[i][j] === 0){
				var items = possible( grid, i, j);
				if(items && items.length < minpossible){
					minx = i; miny = j; minpossible = items.length;
				}
				point[i + ' ' + j] = possible(grid, i, j);
			}
		}
	}
	
	console.log( point );
	grid[minx][miny] = point[minx + ' ' + miny][0];

	for(var i = 0;i < grid.length;i++){
		for(var j = 0;j < grid[0].length;j++){
			if(grid[i][j] === 0){
				var items = possible( grid, i, j);
				if(items && items.length < minpossible){
					minx = i; miny = j; minpossible = items.length;
				}
				point[i + ' ' + j] = possible(grid, i, j);
			}
		}
	}
	console.log('  ');
	console.log( point );

	return grid;
};

solve( grid );
