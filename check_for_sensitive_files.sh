#!/bin/bash

GIT_FILES_CMD="git ls-tree --full-tree -r HEAD"

echo "Check for csv files..."
$GIT_FILES_CMD | grep "csv$"
echo

echo "Check for json files... (only 'package.json' should exist)"
$GIT_FILES_CMD | grep "json$"
