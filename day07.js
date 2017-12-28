const readline = require('readline');

const rl = readline.createInterface({
  input: process.stdin,
});

let nodes = {};

rl.on('line', function(line) {
	let parts = line.split('->');
	let subpart = parts[0].split('(');

	let right = (parts[1] || "").split(',');
	let sons = right[0].length > 0 ? right.map(s => s.trim()) : [];

	let name = subpart[0].trim();
	let weight = Number(subpart[1].split(')')[0].trim());
	nodes[name] = { name, weight, sons };
});

rl.on('close', function() {
	for (let node of Object.keys(nodes)) {
		for (let son of nodes[node].sons) {
			nodes[son].parent = node;
		} 
	}
	let root;
	for (let key of Object.keys(nodes)) {
		let value = nodes[key];
		if(!value.parent) {
			root = value;
			break;
		}
	}

	let max_level = 0;
	let r;
	let xx;
	function f(node, level = 0) {
		let weights = node.sons.map(son => f(nodes[son], level + 1));
		let w;
		if (node["name"] == "fabacam") {
			console.log('xxxxx', node, weights);
		}
		for (weight of weights) {
			if (w && w != weight) {
				if (level > max_level) {
					max_level = level;
					r = node;
					xx = weights;
				}
			}
			w = weight;
		}
		return node.weight + weights.reduce((s,x) => s + x, 0);
	}

	console.log('weight:', f(root));
	console.log(r, xx);
});

