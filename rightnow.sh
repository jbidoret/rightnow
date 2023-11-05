#!/usr/bin/env bash

echo "Hey."
echo "What are you doing right now ? "
read now

cd /your/path/to/now/
source /your/path/to/now/env/activate
rightnow=`python /your/path/to/now/rightnow.py "$now"`

message="Right now: $rightnow"

git add index.html
git commit -m "${message}"
git push

echo "OK."