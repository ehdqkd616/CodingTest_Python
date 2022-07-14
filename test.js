const readline = require('readline');

// 인터페이스 객체를 만들자.
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

let input = [];
rl.on("line", (line) => {
    input.push(line);
    if (input.length === Number(input[0]) + 1) rl.close();
});

rl.on("close", () => {
    for (i in input) {
        console.log(`${input[i]}`);
    }
});