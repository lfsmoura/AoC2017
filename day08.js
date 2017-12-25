
var readline = require('readline');

var rl = readline.createInterface({
  input: process.stdin
});

let lines = [];
rl.on('line', (line) => {
    let parts = line.split(' ');
    lines.push(parts);
});

rl.on('close', () => {
    let vars = {};
    let max = -1;
    for (let part of lines) {
        let op = part[1] == 'inc' ? "+" : "-";
            eval ( `${part[4]} = typeof ${part[4]} == 'undefined' ? 0 : ${part[4]};`);
            eval ( `${part[0]} = typeof ${part[0]} == 'undefined' ? 0 : ${part[0]};`);
            let r = eval ( `if (${part[4]} ${part[5]} ${part[6]} ) ${part[0]} = (${part[0]} || 0) ${op} ${part[2]}`);
        if(r) {
            //max = Math.max(r, max);
            vars[part[0].trim()] = r;
        }
    }
    for (let v of Object.values(vars)){
        max = Math.max(v, max);
    }

    console.log('end', max)
});

