var http = require('http');
var fs = require("fs") ;

fs.readFile('selfIp.txt',"utf8",(err,data)=> {
if (err) {console.log("error");}
ip=data;
http.createServer(function (request, response) {
	var body = "" ;
	if ( request.method == "POST" || request.method == "PUT" ) {
  		request.setEncoding("utf8") ;
  		request.on("data", function(data) {body+=data;} );}

	request.on("end",function() {
		response.writeHead(200, {'Content-Type': 'text/plain'});
		response.end('Ok\n');
		var write = require("fs").writeFile ;
		write("txt_files/message.txt",body,function() {});});
}).listen(8888,ip,function() {

 console.log('Serveur démarré sur le port 8888');

});})
