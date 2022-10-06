process.stdout.write("Hello. What is your name? ")

process.stdin.on('data', (data) => {
    console.log("Hello " + data.toString())
});