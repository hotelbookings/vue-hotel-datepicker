#!/bin/sh

npm run build
git add .
git commit -am "$2"
git push
#git checkout main
#git pull
#git merge summer-booking-progress -X theirs -m "merge sbp"
#git commit -am "$2"
#git tag "$4"
#git push origin "$4"
#git checkout summer-booking-progress
