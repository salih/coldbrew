#!/bin/bash
echo $1
docker run --name $2 -e URL=$1 coldbrew:0.2
cd /home/centos/build/
mkdir $2
docker cp $2:/output /home/centos/build/$2
docker rm $2
echo "Container has been deleted"
cd $2
if grep -q "SUCCESS" output/state.txt; then
echo "Success"
else
echo "Fail"
cd ..
rm -rf $2
fi  
