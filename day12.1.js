const readline = require('readline');

var rl = readline.createInterface({
  input: process.stdin,
});

let G = {
	add(a,b) {
		this[a] = this[a] || [];
		this[b] = this[b] || [];
		this[a].push(b);
		this[b].push(a);
	}
};

rl.on('line', (line) => {
	let parts = line.split('<->');
	let a = parts[0].trim();
	let others = parts[1].split(',').map( s => s.trim());

	for (let x of others) {
		G.add(a,x);
	}
});

rl.on('close', () => {
	const visited = new Map();
	let groups = 0;
		for (let name of Object.keys(G)) {
	let c = 0;
			if (name == "add") continue;
	function visit(a) {
		if (visited[a]) {
			return;
		}
		visited[a] = true;
		c++;
		for (let n of G[a]) {
			visit(n);
		}
	}
	visit(name);
		if (c > 0 ) {
			groups++;
		} 

	console.log('count', c);
	}

	console.log('groups', groups);
});
