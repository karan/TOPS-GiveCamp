var fs = require('fs');
var http = require('http');

var port = 5000;
var PRODUCTION = true;

/* NODE STATIC STUFF
var nodestatic = require('node-static');
var file = new(nodestatic.Server)();


http.createServer(function(req, res) {
	file.serve(req, res);
}).listen(port);

console.log("Listening on " + port);
*/

//var jade = require('jade');


var express = require('express');
var app = express.createServer();
app.use(express.logger());
//app.use(express.static(__dirname));		// DO NOT USE IN PRODUCTION!!!!
app.use('/', express.static('app'));	// SHOULD I USE THIS
//app.set('port', process.env.PORT || 8080);
app.listen(process.env.PORT || port, function() {
	console.log("Listening on " + port);

    app.use('/img', express.static('img'));
    app.use('/lib', express.static('img'));
    app.use('/js', express.static('js'));
    app.use('/css', express.static('css'));
    app.use('/assets', express.static('assets'));
	function addStaticRoute(route, filename) {
		if (!PRODUCTION) {
			filename += ".jade";
		} else {
			filename += ".html";
		}

		app.get(route, function(req, res) {
			//var buf = Buffer(fs.readFileSync('index.html'), 'utf-8');
			//response.send(buf.toString('utf-8'))

			if (PRODUCTION) {
				// for html files
				var data = fs.readFileSync(filename).toString();
				res.send(data);
			} else {
				// for jade files
				res.send( jade.renderFile(filename, ({'pretty': 'true'})) );
				console.log('Routing ' + route + ' to file: ' + filename);
			}
		});
	}
	addStaticRoute('/', 'index');
	/*
	addStaticRoute('/appt', 'appt');
	addStaticRoute('/about', 'about');
	addStaticRoute('/reviews', 'reviews');
	addStaticRoute('/newpatient', 'newpatient');
	addStaticRoute('/location', 'location');
	addStaticRoute('/contact', 'contact');
	addStaticRoute('/joffe', 'joffe');
	addStaticRoute('/branovan', 'branovan');
	*/

});


	/*
app.get('/', function(req, res) {
	data = fs.readFileSync('index.html').toString();
	res.send(data);
});

app.get('/appt', function(req, res) {
	console.log('/appt requested');
	data = fs.readFileSync('appt.html').toString();
	res.send(data);
});
	*/

/*
var app = express(express.logger());

app.get('/', function(request, response) {
	var buf = Buffer(fs.readFileSync('index.html'), 'utf-8');

  response.send(buf.toString('utf-8'))
  //response.send('Hello World 2!');
});

var port = process.env.PORT || 5000;
app.listen(port, function() {
  console.log("Listening on " + port);
});*/
