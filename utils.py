#!/usr/bin/python
import os
DBG = True

__all__ = ['dbgFatal', 'dbgWarn', 'dbgErr', 'dbgInfo']

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
	if value:
		print atype + ':', desc + ' -', str(value)
	else:
		print atype + ':', desc

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
