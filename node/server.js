const http = require("http");
const fs = require("fs");
const os = require("os");
const ip = require("ip");

const server = http.createServer((req, res) => {
    if (req.url === "/") {
    fs.readFile("./Public/index.html", "UTF-8", (err, body) => {
        res.writeHead(200, {"Content-Type": "text/html"});
        res.end(body);
    });
    } else if (req.url.match("/sysinfo")) {
        myHostName=os.hostname();
        seconds=Math.round(process.uptime())
        days=Math.floor(seconds / (3600*24));
        hours=Math.floor(seconds % (3600*24) / 3600);
        min=Math.floor(seconds % 3600 / 60);
        sec=Math.floor(seconds % 60);
        html=`
        <!DOCTYPE html>
        <html>
            <head>
                <title>Node JS Response</title>
            </head>
            <body>
                <p>Hostname: ${myHostName}</p>
                <p>IP: ${ip.address()}</p>
                <p>Server Uptime: Days: ${days} Hours: ${hours} Minutes: ${min} Seconds: ${sec}</p>
                <p>Total Memory: ${((os.totalmem())/1048576).toFixed(3)} MBs</p>
                <p>Free Memory: ${(os.freemem()/1048576).toFixed(2)} MBs</p>
                <p>Number of CPUs: ${(os.cpus()).length} </p>
            </body>
        </html>`
        res.writeHead(200, {"Content-Type": "text/html"});
        res.end(html);
} else {
    res.writeHead(404, {"Content-Type": "text/plain"});
    res.end(`404 File Not Found at ${req.url}`);
}
}).listen(3000);


console.log("Server listening on port 3000")