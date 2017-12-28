
//input = '0	2	7	0';
input = '4	10	4	1	8	4	9	14	5	1	14	15	0	15	3	5';

arr = input.split('\t').map(Number);

let it = 0;
let seen = {};
let cycle_begin = null;
let cycle_size = 0;
while (true) {
	it++;
	let max = arr[0];
	let mi = 0;

	for (let i = 1; i < arr.length; i++) {
		if (arr[i] > max) {
			max = arr[i];
			mi = i;
		}
	}
	arr[mi] = 0;

	let j = 0;
	while (max > 0) {
		j++;
		arr[(j + mi) % arr.length]++;
		max--;
	}
	let joi = arr.join(',');
	
	if (cycle_begin) {
		cycle_size++;
		if (joi === cycle_begin) {
			break;
		}
	} else {
		if (seen[joi]) {
			cycle_begin = joi;
		}
		seen[joi] = true;
	} 
	console.log(cycle_size, arr);
}

console.log('ans', it, cycle_size);
