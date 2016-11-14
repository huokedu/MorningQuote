//Lets require/import the HTTP module
var http = require('http');
var fs = require("fs");
var content = fs.readFileSync("assets/quotes.json");
var template = fs.readFileSync("index.html", 'utf8');

var quotes = JSON.parse(content);

//Lets define a port we want to listen to
const PORT=8080; 

//We need a function which handles requests and send response
function handleRequest(request, response){
	var random = Math.floor((Math.random() * quotes.length + 0));
    response.end(template.replace(/{{quote}}/,quotes[random].text).replace(/{{author}}/,quotes[random].author));
}

//Create a server
var server = http.createServer(handleRequest);

//Lets start our server
server.listen(PORT, function(){
    //Callback triggered when server is successfully listening. Hurray!
    console.log("Server listening on: http://localhost:%s", PORT);
});