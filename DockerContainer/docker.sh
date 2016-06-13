#!/bin/bash

git clone $URL brew-build
mkdir output
cd brew-build
mvn package > output.txt
cd ..
if grep -q "BUILD SUCCESS" brew-build/output.txt; then
	jar_location_text="$(grep 'Building jar' brew-build/output.txt)"
 	
	eo_replace='[INFO] Building jar: '
	tor=''
	jar_location="${jar_location_text/'[INFO] Building jar: /brew-build/'/}"
	mv brew-build/$jar_location output/output.jar 
	rm -rf /brew-build
	cd output
	echo "SUCCESS" > state.txt
else
	rm -rf /brew-build
	cd output
	echo "FAIL" > state.txt
	
fi

