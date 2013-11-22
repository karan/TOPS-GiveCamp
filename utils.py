#!/usr/bin/python
import os
import types

DBG = True
DO_INTROSPECTION = True

if DO_INTROSPECTION:
	import inspect

__all__ = ['dbgFatal', 'dbgWarn', 'dbgErr', 'dbgInfo', 'DBG']

# Colors - *NIX only (http://en.wikipedia.org/wiki/ANSI_escape_code)
if os.name=="posix":
	FATAL_COLOR = '\x1b[91;1m\x1b[7m'	# high intensity red negative
	ERR_COLOR = '\x1b[91;1m'	# high intensity red bold
	WARN_COLOR = '\x1b[93m'	# high intensity orange
	INFO_COLOR = '\x1b[96m'  # high intensity cyan
	END_COLOR = '\x1b[0m'
else:
	FATAL_COLOR = ERR_COLOR = WARN_COLOR = INFO_COLOR = END_COLOR = ''

def dbgFatal(desc, value='', raiseException=False):
	if raiseException:
		raise(makeMsg(FATAL_COLOR + 'FATAL ERROR' + END_COLOR, desc, value))
	else:
		printMsg(FATAL_COLOR + 'FATAL ERROR' + END_COLOR, desc, value)

def dbgErr(desc, value=''):
	printMsg(ERR_COLOR + 'ERROR' + END_COLOR, desc, value)

def dbgWarn(desc, value=''):
	printMsg(WARN_COLOR + 'Warning' + END_COLOR, desc, value)

def dbgInfo(desc, value=''):
	printMsg(INFO_COLOR + 'Info' + END_COLOR, desc, value)

def printMsg(atype, desc, value=''):
	"""Prints a string to stdout with your message"""
	if not DBG: return

	if DO_INTROSPECTION:
		# avoid leaks due to references to frame objects
		frm = inspect.stack()[2]
		try:
			#module_name, _, function_name = inspect.getmodule(frm)
			module_name = frm[1]
			line_number = str(frm[2])
			function_name = frm[3]
			module_and_caller = "[" + module_name + " " + line_number + " -> " + function_name + "] "
		finally:
			del frm
	else:
		module_and_caller = ''

	if value:
		if type(value) == types.UnicodeType:
			print atype + ':', module_and_caller + desc + ' -', unicode(value)
		else:
			print atype + ':', module_and_caller + desc + ' -', str(value)
	else:
		print atype + ':', module_and_caller + desc

def makeMsg(atype, desc, value=''):
	"""Return a string with your message"""
	if value:
		return Exception(atype + ': '+ desc + ' - ' + str(value))
	else:
		return Exception(atype + ': ' + desc)


def main():
	dbgInfo('testing', 'value')
	dbgWarn('testing', 'value')
	dbgErr('testing', 'value')
	dbgFatal('testing', 'value')
	return 0

if __name__ == '__main__':
	import sys
	sys.exit(main())
