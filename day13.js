const assert = require("assert");

function sev(scans) {
    let state = scans.map(x => 0);
    let dir = scans.map(x => -1);
    let s = 0;
    for (let current = 0; current <= scans.length; current++) {
        console.log(state[current])
        if (state[current] == 0) {
            console.log('caught')
            s += scans[current] * current;
        }

        for (let i = 0; i < scans.length; i++) {
            if (state[i] == scans[i] - 1 || state[i] == 0) {
                dir[i] *= -1;
            }
            state[i] += dir[i];
        }
        let x = scans.map( x=> 0)
        x[current] = 1;
        console.log(x);
        console.log(state)
    }
    return s;
}

assert.strictEqual(sev([3,2,undefined,undefined,4,undefined,4]), 24);

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
    console.log('a', sev(arr))
});