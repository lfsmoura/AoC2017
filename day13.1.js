const assert = require("assert");

function sev(scans, delay = 0) {
    if (delay % 10000 == 0) console.log(delay)
    for (let current = 0; current <= scans.length; current++) {
        if (! scans[current]) {
            continue;
        }
        let steps = current + delay;
        if (steps % (2 * (scans[current] - 1)) == 0) {
            return 1;
        }
    }
    return 0;
}

function pico(scans) {
    let i = 0;
    while (sev(scans, ++i)) {}
    return i;
}
assert.strictEqual(pico([3,2,undefined,undefined,4,undefined,4]), 10);

const readline = require('readline');

var rl = readline.createInterface({
  input: process.stdin,
});

let arr = [];
rl.on('line', (line) => {
    let [a,b] = line.split(":").map(Number);
    arr[a] = b;
});

rl.on('close', (line) => {
    console.log(arr)
    console.log('a', pico(arr))
});