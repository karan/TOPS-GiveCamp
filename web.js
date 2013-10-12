var fs = require('fs');
var http = require('http');
var port = process.env.PORT || 9001;
var PRODUCTION = true;


//var jade = require('jade');


var express = require('express');
var app = express.createServer();
app.use(express.logger());
app.use('/', express.static('app'));

// Assets
app.use('/img', express.static('img'));
app.use('/lib', express.static('img'));
app.use('/js', express.static('js'));
app.use('/css', express.static('css'));
app.use('/assets', express.static('assets'));

app.use(express.bodyParser({ keepExtensions: true, uploadDir: 'uploads' }));


function addUploadRoute() {
	app.post('/upload', function(req, res) {
		var NUM_FILES = 3;
		var UPLOAD_DIR = "uploads";
		var csvfilenames = ['communityFile', 'memberFile', 'servicesFile' ];

		for (var i = 0; i < NUM_FILES; i++) {
			var fileObject = req.files[ csvfilenames[i] ];

			if (!fileObject) {
				var err = "ERROR: " + csvfilenames[i] + "DOES NOT EXIST";
				console.log(err);
				res.send(err);
				return;
			} else {
				console.log("File1: name = " + fileObject.name + "| path = " + fileObject.path);
				fs.readFile(fileObject.path, function (err, data) {
					if (err) console.log(err);
					/*
					var newPath = __dirname + UPLOAD_DIR + fileObject.name;
					fs.writeFile(newPath, data, function (err) {
						if (err) throw err;
						console.log(err);
						res.redirect("back");
					});
					*/
				});
			}
		}

		console.log("Done with files");
		res.redirect("back");
	}); // app.post()
}

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
addUploadRoute();

app.listen(port, function() {
	console.log("Listening on " + port);
});
