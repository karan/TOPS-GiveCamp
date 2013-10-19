var sys = require('sys');
var exec = require('child_process').exec;

function processData(filenames) {
	// add arg parser
	// get test data to try it out on
	var processCmd = "./process.py " + filenames[0] + " " + filenames[1] + " " + filenames[2];
	console.log("Running cmd: " + processCmd);
	exec(processCmd, cmdOutputCallback);
}

function convertToJSON() {
	exec("./csvtojson.py", cmdOutputCallback);
}

function cmdOutputCallback(err, stdout, stderr) {
	if (err) sys.puts("(processWrapper.js) Err: " + err);
	if (stdout) sys.puts("(processWrapper.js) stdout: " + err);
	if (stderr) sys.puts("(processWrapper.js) stderr: " + err);
}

exports.processData = processData;
exports.convertToJSON = convertToJSON;

//processData();
