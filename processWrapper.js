var sys = require('sys');
var PRODUCTION = false;

var useAsyncExec = false;
if (useAsyncExec) {
	var exec = require('child_process').exec;
} else {
	var sh = require('execSync');	// synchronous command execution
}

exports.processData = processData;
exports.convertToJSON = convertToJSON;
exports.previewEmail = previewEmail;

function previewEmail() {
	var processCmd = "./process.py " + "--preview";
	console.log("Running cmd: " + processCmd);
	exec(processCmd, cmdOutputCallback);
}

function processData(filenames) {
	// add arg parser
	// get test data to try it out on
	var processCmd = "./process.py " + filenames[0] + " " + filenames[1] + " " + filenames[2];
	console.log("Running cmd: " + processCmd);
	exec(processCmd, cmdOutputCallback);
}

function convertToJSON() {
	var processCmd = "./csvtojson.py";
	exec(processCmd, cmdOutputCallback);
}

function exec(cmd, cmdOutputCallback) {
	if (useAsyncExec) {		// asynchronous command execution - default in node
		var execAsync = require('child_process').exec;
		execAsync(processCmd, cmdOutputCallback);
	} else {
		if (!PRODUCTION) {
			var result = sh.run(cmd);
			console.log("Ran command: " + cmd + " which exited with code: " + result.code + " and output: " + result.stdout);
		} else if (PRODUCTION) {
			var code = sh.run(cmd);
			console.log("Ran command: " + cmd + " which exited with code: " + code);
		}
	}
}


// for child_process (async)
function cmdOutputCallback(err, stdout, stderr) {
	if (err) sys.puts("(processWrapper.js) Err: " + err);
	if (stdout) sys.puts("(processWrapper.js) stdout: " + err);
	if (stderr) sys.puts("(processWrapper.js) stderr: " + err);
}

