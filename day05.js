const readline = require('readline');

const rl = readline.createInterface({
  input: process.stdin,
});

let list = [];

rl.on('line', function(line) {
	list.push(parseInt(line));
});

rl.on('close', function() {
	let i = 0;
	let steps = 0;
	while(true) {
		steps++;
		let jump = list[i];
		list[i] += list[i] >= 3 ? - 1 : 1;  
		i += jump;
		if (i < 0 || i >= list.length) {
			break;
		}
	}
	console.log(steps, list);
});
