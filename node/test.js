const path = require("path");



console.log("Using PATH Module:");
console.log(`Hello from file ${path.basename(__filename)}`);
console.log(`Process args: ${process.argv}`)