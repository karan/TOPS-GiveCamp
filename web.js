var fs = require('fs');
var http = require('http');
var port = process.env.PORT || 9001;
var PRODUCTION = false;

//var jade = require('jade');
var express = require('express');
var backendWrapper = require('./processWrapper');
var app = express.createServer();
app.use(express.logger());
app.use('/', express.static('app'));

// Assets
app.use('/img', express.static('img'));
app.use('/lib', express.static('img'));
app.use('/js', express.static('js'));
app.use('/css', express.static('css'));
app.use('/assets', express.static('assets'));

app.use(express.bodyParser({ keepExtensions: true, uploadDir: 'initial-uploads' }));


function addUploadRoute() {
	app.post('/upload', function(req, res) {
		var NUM_FILES = 3;
		var UPLOAD_DIR = "app/uploads";
		var csvfilenames = ["communityFile", "memberFile", "servicesFile" ];
		//console.log("REQUEST: " + req);

		for (var i = 0; i < NUM_FILES; i++) {
			var fileObject = req.files[ csvfilenames[i] ];
			var filename = csvfilenames[i];

			if (!fileObject) {
				var err = "ERROR: " + csvfilenames[i] + " DOES NOT EXIST";
				console.log(err);

				if (!PRODUCTION) continue;
				else res.send(err);
				// return;
			} else {
				console.log("(node: in /upload route) Processing: " + csvfilenames[i]);
				console.log("File: name = " + fileObject.name + "| path = " + fileObject.path);
				fs.readFile(fileObject.path, function (err, data) {
					if (err) console.log(err);
					var newPath = __dirname + "/" + UPLOAD_DIR + "/" + filename + ".csv";
					console.log("writing file: " + newPath);
					fs.writeFile(newPath, data, function (err) {
						if (err) console.log("Error writing file: " + err);
						else console.log("wrote file successfully");
						//res.redirect("back");
					});
				});
			}
		} 	// end of for-loop processing 3 files

		console.log("Done with files. Starting processing...");
		backendWrapper.processData();
		console.log("finished postprocessing (process.py) successfully");
		res.redirect('/#/edit');
		//res.redirect("back");
	}); // app.post()
}

function addStaticRoute(route, filename) {
	if (false) {
		filename += ".jade";
	} else {
		filename += ".html";
	}

	app.get(route, function(req, res) {
		//var buf = Buffer(fs.readFileSync('index.html'), 'utf-8');
		//response.send(buf.toString('utf-8'))

		if (true) {
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
