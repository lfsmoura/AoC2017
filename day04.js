const readline = require('readline');

const rl = readline.createInterface({
  input: process.stdin,
});

let valid = 0;

rl.on('line', function(line) {
	let words = line.split(' ');
	words.sort();
	
	let last_word = '*';
	for (word of words) {
		if (word === last_word) {
			return;
		}
		last_word = word;
	}
	valid++;
});

rl.on('close', function() {
	console.log('valid:', valid);
});
