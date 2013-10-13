#!/bin/bash

echo "find conflicts in curdir"
grep HEAD *.{py,js,sh,css,txt,html,md,json}

echo "find conflicts in special files"
grep HEAD Procfile
grep HEAD .gitignore


echo "find conflicts in app/ - one level down"
grep HEAD app/*.{py,js,sh,css,txt,html,md,json}

echo "find conflicts in assets/ - one level down"
grep HEAD assets/*.{py,js,sh,css,txt,html,md,json}

echo "find conflicts in app/ -two levels down"
grep HEAD app/*/*.{py,js,sh,css,txt,html,md,json}
