//create a demo server application

const http = require('http');

const hostname = '127.0.0.1';
const port = 3000;

const msg = "Hello World";

const server = http.createServer((req, res) => {
    res.statusCode = 200;
    res.setHeader('Content-Type', 'text/plain');
    res.end(msg);
})
server.listen(port, hostname, () => {
    console.log(`Server running at http://${hostname}:${port}/`);
}
);

